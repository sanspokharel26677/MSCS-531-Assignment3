import matplotlib.pyplot as plt
import numpy as np

# Data for cache types
cache_types = ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']

# Data for each run (Cache Hits)
cache_hits_run1 = [1890, 7056, 1]
cache_hits_run2 = [1936, 7143, 3]
cache_hits_run3 = [1938, 7143, 8]

# Data for each run (Cache Misses)
cache_misses_run1 = [135, 230, 364]
cache_misses_run2 = [89, 143, 229]
cache_misses_run3 = [88, 143, 163]

# Data for each run (Cache Miss Rate %)
cache_miss_rate_run1 = [6.67, 3.16, 99.73]
cache_miss_rate_run2 = [4.39, 1.96, 98.71]
cache_miss_rate_run3 = [4.34, 1.96, 95.30]

# Data for each run (Average Miss Latency in ticks)
miss_latency_run1 = [83844.44, 79067.39, 78516.48]
miss_latency_run2 = [87224.72, 86835.66, 85438.86]
miss_latency_run3 = [83292.13, 86835.66, 85862.00]

# Set up positions for each group of bars
x = np.arange(len(cache_types))
width = 0.2  # Width of the bars

# 1. Plotting Cache Hits
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, cache_hits_run1, width, label='Run 1 (Initial)')
rects2 = ax.bar(x, cache_hits_run2, width, label='Run 2 (2MB L2 Cache)')
rects3 = ax.bar(x + width, cache_hits_run3, width, label='Run 3 (4MB L2 + Prefetcher)')
ax.set_xlabel('Cache Type')
ax.set_ylabel('Cache Hits')
ax.set_title('Cache Hits Comparison Across Three Runs')
ax.set_xticks(x)
ax.set_xticklabels(cache_types)
ax.legend()
plt.tight_layout()
plt.savefig('cache_hits_comparison.png')

# 2. Plotting Cache Misses
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, cache_misses_run1, width, label='Run 1 (Initial)')
rects2 = ax.bar(x, cache_misses_run2, width, label='Run 2 (2MB L2 Cache)')
rects3 = ax.bar(x + width, cache_misses_run3, width, label='Run 3 (4MB L2 + Prefetcher)')
ax.set_xlabel('Cache Type')
ax.set_ylabel('Cache Misses')
ax.set_title('Cache Misses Comparison Across Three Runs')
ax.set_xticks(x)
ax.set_xticklabels(cache_types)
ax.legend()
plt.tight_layout()
plt.savefig('cache_misses_comparison.png')

# 3. Plotting Cache Miss Rate
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, cache_miss_rate_run1, width, label='Run 1 (Initial)')
rects2 = ax.bar(x, cache_miss_rate_run2, width, label='Run 2 (2MB L2 Cache)')
rects3 = ax.bar(x + width, cache_miss_rate_run3, width, label='Run 3 (4MB L2 + Prefetcher)')
ax.set_xlabel('Cache Type')
ax.set_ylabel('Cache Miss Rate (%)')
ax.set_title('Cache Miss Rate Comparison Across Three Runs')
ax.set_xticks(x)
ax.set_xticklabels(cache_types)
ax.legend()
plt.tight_layout()
plt.savefig('cache_miss_rate_comparison.png')

# 4. Plotting Average Miss Latency
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, miss_latency_run1, width, label='Run 1 (Initial)')
rects2 = ax.bar(x, miss_latency_run2, width, label='Run 2 (2MB L2 Cache)')
rects3 = ax.bar(x + width, miss_latency_run3, width, label='Run 3 (4MB L2 + Prefetcher)')
ax.set_xlabel('Cache Type')
ax.set_ylabel('Average Miss Latency (ticks)')
ax.set_title('Average Miss Latency Comparison Across Three Runs')
ax.set_xticks(x)
ax.set_xticklabels(cache_types)
ax.legend()
plt.tight_layout()
plt.savefig('average_miss_latency_comparison.png')

# Show all plots (optional)
plt.show()

