# Brackets in Matrix Chain Multiplication 🧮

**Difficulty:** Hard  
**Accuracy:** 59.66%  
**Submissions:** 39K+  
**Points:** 8  
**Average Time:** 25m  

---

## Problem Statement

Given an array **arr[]** of length **n** used to denote the dimensions of a series of matrices such that the dimension of *i*-th matrix is `arr[i] x arr[i+1]`.  

There are a total of `n - 1` matrices. Find the most efficient way to multiply these matrices together.

Your task is to return the **string** which is formed of **A–Z** (only uppercase) denoting matrices & **Brackets** `"(" ")"` denoting multiplication symbols.  

For example, if `n = 11`, the matrices can be denoted as `A - K` as `n <= 26` and multiplication of `A` and `B` is denoted as `(AB)`.

---

## NOTE

1. Each multiplication is denoted by putting **open & closed brackets** to the matrices multiplied  
   & also, please note that the order of matrix multiplication matters,  
   as matrix multiplication is **non-commutative**: `A*B != B*A`.

2. As there can be **multiple possible answers**, the console would print `"true"` for the correct string and `"false"` for the incorrect string.  
   You need to only return a string that performs a **minimum number of multiplications**.

---

## Examples

### Example 1

**Input:** `arr[] = [40, 20, 30, 10, 30]`  
**Output:** `true`  

**Explanation:**  
Let’s divide this into matrix/only 4 are possible:  
`[40, 20] -> A`, `[20, 30] -> B`, `[30, 10] -> C`, `[10, 30] -> D`  

First we perform multiplication of `B & C -> (BC)`, then we multiply `A` to `(BC) -> (A(BC))`, then we multiply `D` to `(A(BC)) -> ((A(BC))D)`  

So the solution returned the string `((A(BC))D)`, which performs minimum multiplications.  

The total number of multiplications are:  

`20*30*10 + 40*20*10 + 40*10*30 = 26,000`.

---

### Example 2

**Input:** `arr[] = [10, 20, 30]`  
**Output:** `true`  

**Explanation:**  
There is only one way to multiply two matrices: `(AB)`.  
The cost for the multiplication will be `6000`.

---

### Example 3

**Input:** `arr[] = [10, 20, 30, 40]`  
**Output:** `true`  

**Explanation:**  
There are two possible ways to multiply three matrices:

- `((AB)C)`: The cost for the multiplication will be `18,000`.  
- `(A(BC))`: The cost for the multiplication will be `32,000`.  

So the solution returned the string `((AB)C)`, which performs minimum multiplications.

---

## Constraints

- \( 2 \le \text{arr.size()} \le 50 \)  
- \( 1 \le \text{arr}[i] \le 100 \)

---

## Expected Complexities

- **Time Complexity:** `O(n^3)`  
- **Auxiliary Space:** `O(n^2)`

---

## Company Tags

- Microsoft  

---

## Topic Tags

- Dynamic Programming  
- Matrix  
- Data Structures  
- Algorithms  

---

## Related Interview Experiences

- Microsoft Interview Experience Set 128 Campus Internship  

---

## Related Articles

- Printing Brackets Matrix Chain Multiplication Problem  

---

---

Got it — we’ll drop the **Type** dropdown and instead:

* You pick **Market**.
* The **Ticker** dropdown automatically lists **all tickers in that market**, from both `equities` and `indices`.
* Internally we remember which ticker belongs to which kind folder so we can load:

  * price from `.../yf_stockdata/<market>/<equities|indices>/<ticker>/...`
  * news from `.../news/<market>/<equity|index>/<ticker>/...`

Here’s the updated app as a single file.

---

## New file (no “Type” dropdown)

Save as, or overwrite:

```text
C:\Users\debda\Documents\GitHub\data_collection\web_dashboard\market_ticker_news_1min.py
```

```python
from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Tuple
from datetime import date

import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# ---------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------

# This file lives in: <repo_root>/web_dashboard/market_ticker_news_1min.py
THIS_DIR = Path(__file__).resolve().parent

# Price data base dir: <repo_root>/stock_package/data/yf_stockdata
PRICE_BASE_DIR = THIS_DIR.parent / "stock_package" / "data" / "yf_stockdata"

# News data base dir: <repo_root>/stock_package/data/news
NEWS_BASE_DIR = THIS_DIR.parent / "stock_package" / "data" / "news"

# Folder name for 1-minute interval in yf_stockdata
INTERVAL_FOLDER = "1min"

# Map between price "kind" folder and news "type" folder
PRICE_KIND_FOLDERS = ["equities", "indices"]
NEWS_KIND_MAP = {
    "equities": "equity",
    "indices": "index",
}


# ---------------------------------------------------------
# Helper functions: filesystem discovery
# ---------------------------------------------------------

def list_dirs(path: Path) -> List[str]:
    if not path.exists():
        return []
    return sorted([d.name for d in path.iterdir() if d.is_dir()])


def get_markets() -> List[str]:
    """All markets under yf_stockdata."""
    return list_dirs(PRICE_BASE_DIR)


def get_kind_folders_for_market(market: str) -> List[str]:
    """Which of ['equities', 'indices'] exist for this market."""
    present = []
    for folder in PRICE_KIND_FOLDERS:
        if (PRICE_BASE_DIR / market / folder).exists():
            present.append(folder)
    return present


def get_all_tickers_for_market(market: str) -> Tuple[List[str], Dict[str, str]]:
    """
    Return (sorted_tickers, ticker_to_kind_folder_map) for a market.

    Tickers are gathered from both 'equities' and 'indices'.
    If a ticker appears in more than one kind, the last one wins.
    """
    kind_folders = get_kind_folders_for_market(market)
    ticker_to_kind: Dict[str, str] = {}

    for kind_folder in kind_folders:
        kind_dir = PRICE_BASE_DIR / market / kind_folder
        if not kind_dir.exists():
            continue
        for ticker_dir in kind_dir.iterdir():
            if not ticker_dir.is_dir():
                continue
            ticker_to_kind[ticker_dir.name] = kind_folder

    tickers = sorted(ticker_to_kind.keys())
    return tickers, ticker_to_kind


def list_dates_for_ticker(
    market: str,
    kind_folder: str,
    ticker: str,
) -> List[date]:
    """
    Return all calendar dates for which a 1min stock.csv exists
    for this market/kind/ticker.
    """
    ticker_dir = PRICE_BASE_DIR / market / kind_folder / ticker
    if not ticker_dir.exists():
        return []

    dates: List[date] = []
    for year_dir in ticker_dir.iterdir():
        if not year_dir.is_dir():
            continue
        for month_dir in year_dir.iterdir():
            if not month_dir.is_dir():
                continue
            for day_dir in month_dir.iterdir():
                if not day_dir.is_dir():
                    continue
                csv_file = day_dir / INTERVAL_FOLDER / "stock.csv"
                if csv_file.exists():
                    try:
                        d = date(
                            int(year_dir.name),
                            int(month_dir.name),
                            int(day_dir.name),
                        )
                        dates.append(d)
                    except ValueError:
                        continue

    return sorted(set(dates))


@st.cache_data(show_spinner=True)
def load_day_price_data(
    market: str,
    kind_folder: str,
    ticker: str,
    d: date,
) -> pd.DataFrame:
    """
    Load a single day's 1min stock.csv for the given ticker.
    """
    year = f"{d.year:04d}"
    month = f"{d.month:02d}"
    day = f"{d.day:02d}"

    csv_path = (
        PRICE_BASE_DIR
        / market
        / kind_folder
        / ticker
        / year
        / month
        / day
        / INTERVAL_FOLDER
        / "stock.csv"
    )

    if not csv_path.exists():
        return pd.DataFrame()

    df = pd.read_csv(csv_path)

    if "Datetime" in df.columns:
        # Interpret as UTC and strip tz to get naive UTC timestamps
        df["Datetime"] = pd.to_datetime(df["Datetime"], utc=True).dt.tz_localize(None)

    return df


# ---------------------------------------------------------
# News loader
# ---------------------------------------------------------

@st.cache_data(show_spinner=True)
def load_news_for_date(
    market: str,
    kind_folder: str,
    ticker: str,
    d: date,
) -> List[Dict]:
    """
    Load news for the given (market, kind, ticker, date) from:

      stock_package/data/news/<MARKET>/<equity|index>/<TICKER>/YYYY/MM/DD/news.csv

    Returns list of dicts:
      { "datetime": naive UTC datetime, "title", "publisher", "link" }
    """
    news_type = NEWS_KIND_MAP.get(kind_folder)
    if news_type is None:
        return []

    year = f"{d.year:04d}"
    month = f"{d.month:02d}"
    day = f"{d.day:02d}"

    csv_path = NEWS_BASE_DIR / market / news_type / ticker / year / month / day / "news.csv"
    if not csv_path.exists():
        return []

    df = pd.read_csv(csv_path)

    # Example columns:
    # unix_time,datetime_utc,title,url,publisher,summary,type,source
    if "datetime_utc" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime_utc"], utc=True).dt.tz_localize(None)
    elif "unix_time" in df.columns:
        df["datetime"] = pd.to_datetime(df["unix_time"], unit="s", utc=True).dt.tz_localize(None)
    else:
        return []

    # Deduplicate, typically by url to remove RSS/STORY duplicates
    if "url" in df.columns:
        df = df.drop_duplicates(subset=["url"])
    else:
        df = df.drop_duplicates(subset=["title", "datetime"])

    df = df.sort_values("datetime")

    news = []
    for _, row in df.iterrows():
        news.append(
            {
                "datetime": row["datetime"],
                "title": str(row.get("title", "")),
                "publisher": str(row.get("publisher", "")),
                "link": str(row.get("url", "")),
            }
        )

    return news


# ---------------------------------------------------------
# Plotly figure builder
# ---------------------------------------------------------

def build_figure(
    df_price: pd.DataFrame,
    news_points: List[Dict],
    ticker: str,
) -> go.Figure:
    """Create a Plotly figure with a 1-min price line and news markers."""
    fig = go.Figure()

    # Price line
    if not df_price.empty:
        fig.add_trace(
            go.Scatter(
                x=df_price["Datetime"],
                y=df_price["Close"],
                mode="lines",
                name=f"{ticker} Close",
                line=dict(width=2),
            )
        )

    # News markers aligned to nearest price point
    news_x = []
    news_y = []
    news_text = []

    if not df_price.empty and news_points:
        price_series = df_price.set_index("Datetime")["Close"]

        for item in news_points:
            t = item["datetime"]
            if t < price_series.index.min() or t > price_series.index.max():
                # Skip articles far outside the intraday range
                continue

            idx_pos = price_series.index.get_indexer([t], method="nearest")[0]
            t_near = price_series.index[idx_pos]
            y_val = float(price_series.iloc[idx_pos])

            news_x.append(t_near)
            news_y.append(y_val)
            news_text.append(item["title"])

        if news_x:
            fig.add_trace(
                go.Scatter(
                    x=news_x,
                    y=news_y,
                    mode="markers",
                    name="News",
                    marker=dict(size=9, symbol="triangle-up", color="red"),
                    text=news_text,
                    hovertemplate="%{text}<br>%{x}<extra></extra>",
                )
            )

    fig.update_layout(
        xaxis=dict(title="Time"),
        yaxis=dict(title="Close"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
        margin=dict(l=40, r=40, t=40, b=40),
        height=600,
    )

    return fig


# ---------------------------------------------------------
# Streamlit app
# ---------------------------------------------------------

def main() -> None:
    st.set_page_config(page_title="1min Price + Local News", layout="wide")
    st.title("📈 1-Minute Price with Local News")

    if not PRICE_BASE_DIR.exists():
        st.error(f"Price data directory not found: {PRICE_BASE_DIR}")
        st.stop()

    # ---- Sidebar: market, ticker, date ----

    markets = get_markets()
    if not markets:
        st.error("No markets found under yf_stockdata.")
        st.stop()

    market = st.sidebar.selectbox("Market", markets)

    tickers, ticker_to_kind = get_all_tickers_for_market(market)
    if not tickers:
        st.error(f"No tickers found for market {market}.")
        st.stop()

    ticker = st.sidebar.selectbox("Ticker", tickers)
    kind_folder = ticker_to_kind[ticker]

    dates = list_dates_for_ticker(market, kind_folder, ticker)
    if not dates:
        st.error("No 1-minute data found for this selection.")
        st.stop()

    selected_date = st.sidebar.selectbox(
        "Date (1-min data)",
        dates,
        format_func=lambda d: d.strftime("%Y-%m-%d"),
    )

    st.sidebar.markdown(
        f"Price: `stock_package/data/yf_stockdata/{market}/{kind_folder}/{ticker}`\n\n"
        f"News:  `stock_package/data/news/{market}/{NEWS_KIND_MAP.get(kind_folder, '?')}/{ticker}`"
    )

    # ---- Load data ----

    with st.spinner("Loading price data..."):
        df_price = load_day_price_data(market, kind_folder, ticker, selected_date)

    if df_price.empty:
        st.warning("Could not load price data for this date.")
        st.stop()

    with st.spinner("Loading local news..."):
        news_points = load_news_for_date(market, kind_folder, ticker, selected_date)

    st.write(
        f"Showing **{ticker}** in **{market}** "
        f"for **{selected_date.strftime('%Y-%m-%d')}**"
    )

    # ---- Plot ----

    fig = build_figure(df_price, news_points, ticker)
    st.plotly_chart(fig, use_container_width=True)

    # ---- News table ----

    if news_points:
        st.subheader("News (local CSV)")
        news_df = pd.DataFrame(
            [
                {
                    "datetime_utc": n["datetime"],
                    "title": n["title"],
                    "publisher": n["publisher"],
                    "link": n["link"],
                }
                for n in news_points
            ]
        )
        st.dataframe(news_df)
    else:
        st.info("No news CSV found or no rows for this date.")


if __name__ == "__main__":
    main()
```

---

## How to run

From your repo root:

```bash
cd C:\Users\debda\Documents\GitHub\data_collection
streamlit run web_dashboard\market_ticker_news_1min.py
```

Now the sidebar just has:

* **Market** (e.g. `IND`, `US`)
* **Ticker** (equities + indices for that market)
* **Date (1-min data)**

and the app figures out the right `equities/indices` + `equity/index` paths automatically.

---

---

I’m going to assume you’re talking about the **Sliding Window technique** (very common interview topic, and it fits nicely with stock / time-series data you’re working with). I’ll:

1. Give a few **real-world use cases** that are easy to mention in interviews.
2. Provide a **full Python program** that uses sliding window to solve a classic problem (max sum subarray of size `k`), with **inline time/space complexity comments for each important step**, sample input/output, and a `timeit` measurement in `main`.

---

## 5. Real-World Use Cases (Sliding Window)

1. **Stock analytics (moving averages / indicators)**

   * Compute 5-minute / 20-minute moving averages for stock prices using a sliding window over time-ordered price data.
   * Same technique for volume, volatility, etc.
   * Interview hook: “The same logic used for moving averages in trading platforms.”

2. **Real-time monitoring (servers / websites / APIs)**

   * Track the number of requests in the last 1 minute / 5 minutes to detect spikes (DoS attacks, traffic anomalies).
   * Sliding window over timestamps of incoming requests.
   * Interview hook: “How would you implement rate limiting or alert when QPS exceeds a threshold?”

3. **Streaming sensor / IoT data**

   * Monitor temperature, CPU usage, heart-rate, etc. over the last N readings and compute metrics: max, min, average, standard deviation.
   * Window moves as new sensor readings arrive.
   * Interview hook: “Processing continuous data streams with bounded memory.”

4. **String / text problems**

   * Longest substring without repeating characters (unique-character window).
   * Smallest substring containing all characters of a pattern (anagram / window-count problems).
   * Interview hook: “Very common LeetCode-style questions.”

These are all easy to explain to an interviewer and clearly show *why* sliding window is useful.

---

## 6. Full Program (with complexity comments + `timeit`)

### Problem:

Given an array of integers and an integer `k`, find the **maximum sum** of any contiguous subarray of size `k` using the **sliding window** technique.

* **Input example**: `arr = [2, 1, 5, 1, 3, 2]`, `k = 3`
* **Output**: `9` (subarray `[5, 1, 3]`)

```python
"""
Sliding Window example:
Find maximum sum of any contiguous subarray of size k.

We also:
- Show step-by-step time/space complexity in comments.
- Use timeit.default_timer to measure runtime of the full program.
"""

from __future__ import annotations

from typing import List
import timeit


def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Compute the maximum sum of any contiguous subarray of size k.

    Sliding window idea:
    - Compute sum of first k elements.
    - Then slide the window by 1 element at a time:
      subtract the element leaving the window, add the new element entering.

    Time Complexity:  O(n)  where n = len(arr)
      - We visit each element at most twice (once when it enters the window, once when it leaves).
    Space Complexity: O(1)
      - We use a few integer variables; no extra data structures proportional to n.
    """
    n = len(arr)

    # Edge case check
    # Time: O(1), Space: O(1)
    if k <= 0 or k > n:
        raise ValueError("k must be between 1 and len(arr)")

    # Step 1: compute the sum of the first window of size k
    # Time: O(k) for summation
    # Space: O(1)
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: slide the window from index 1 to n - k
    # Loop runs (n - k) times -> Time: O(n - k) = O(n)
    # Each iteration is O(1)
    for i in range(k, n):
        # subtract element leaving the window, add element entering the window
        # both O(1)
        window_sum += arr[i] - arr[i - k]

        # update max_sum if needed (O(1))
        if window_sum > max_sum:
            max_sum = window_sum

    # Final answer (O(1))
    return max_sum


def main() -> None:
    # Example input for demonstration
    # Time: O(1) to define
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    # Actual algorithm execution
    # Overall Time: O(n)
    result = max_sum_subarray(arr, k)

    # Output (O(1))
    print(f"Input array: {arr}")
    print(f"k = {k}")
    print(f"Maximum sum of any contiguous subarray of size {k}: {result}")


if __name__ == "__main__":
    # Measure runtime of the full program using timeit.default_timer
    start_time = timeit.default_timer()  # O(1)

    main()  # This runs our example once

    end_time = timeit.default_timer()  # O(1)

    # Total execution time (O(1))
    elapsed = end_time - start_time
    print(f"\nTotal runtime (seconds): {elapsed:.8f}")
```

### What this program does

1. **Defines** `max_sum_subarray` using sliding window:

   * First sum of initial window: `sum(arr[:k])`
   * For each new index `i` from `k` to `n-1`, update the window in O(1):

     * `window_sum += arr[i] - arr[i-k]`
   * Track `max_sum`.

2. **In `main()`**:

   * Uses sample input `arr = [2, 1, 5, 1, 3, 2]`, `k = 3`.
   * Prints:

     ```text
     Input array: [2, 1, 5, 1, 3, 2]
     k = 3
     Maximum sum of any contiguous subarray of size 3: 9
     ```

3. In the `if __name__ == "__main__":` block:

   * Uses `timeit.default_timer()` to measure how long `main()` took, and prints:

     ```text
     Total runtime (seconds): 0.00000xx
     ```

You can easily plug in larger arrays (e.g., 10⁵ or 10⁶ elements) to show **O(n)** behavior, and in an interview you can tie this directly to:

* Moving averages on stock price series,
* Monitoring rolling metrics over logs or sensor streams,
* And classic sliding-window string problems.
