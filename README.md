# Cache Performance Visualization

This Python script generates visual comparisons of cache performance across three different simulation runs. It compares **Cache Hits**, **Cache Misses**, **Cache Miss Rate**, and **Average Miss Latency** for the **L1 Data Cache**, **L1 Instruction Cache**, and **L2 Cache** across the following three simulation configurations:
1. **Run 1**: Initial run with default cache settings.
2. **Run 2**: Modified configuration with a 2MB L2 cache.
3. **Run 3**: Modified configuration with a 4MB L2 cache and a Stride Prefetcher.

## Files Generated
The script generates four PNG images, each representing a comparison between the three simulation runs:
- `cache_hits_comparison.png`: Cache Hits Comparison
- `cache_misses_comparison.png`: Cache Misses Comparison
- `cache_miss_rate_comparison.png`: Cache Miss Rate Comparison
- `average_miss_latency_comparison.png`: Average Miss Latency Comparison

## Dependencies
This script requires Python 3 and the following Python packages:
- `matplotlib`: For generating and saving the plots.
- `numpy`: For handling numeric data and bar positions in the plots.

### You can install the necessary packages using pip:
pip install matplotlib numpy

# Running the Script
1. Clone or download this repository to your local machine.
2. Navigate to the directory where the script is saved.
3. Run the Python script to generate and save the plots:
python cache_performance_comparison.py or python3 cache_performance_comparison.py  depending on your configuration

# What the Script Does
Cache Hits: Visualizes the cache hits for L1 Data Cache, L1 Instruction Cache, and L2 Cache across all three runs.
Cache Misses: Compares the number of cache misses for each cache type.
Cache Miss Rate: Shows the percentage of cache misses.
Average Miss Latency: Displays the average latency in ticks for cache misses.
All the plots are saved in the current directory as PNG images. You can modify the filenames or paths in the script if you want to save them elsewhere.
