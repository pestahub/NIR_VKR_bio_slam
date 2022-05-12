### Как делать анализ результатов

```
source scripts/venv/bin/activate
```

```
rosbag record /odom_incremental /odom/ground_truth 

cp 2022-05-12-17-58-37.bag lio_sam_line_01noise_01drift.bag

evo_ape bag lio_sam_line_01noise_01drift.bag /odom/ground_truth /odom_incremental -va --plot --plot_mode xy --save_results results/lio_sam_line_01noise_01drift.zip

evo_res --use_filenames results/lio_sam_line_01noise_01drift.zip results/lio_sam_line_001noise_01drift.zip -p --save_table results/lio_sam_line_2.csv



```