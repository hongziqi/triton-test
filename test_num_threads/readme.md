## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_num_threads > test_num_threads.log
```

### 统计结果
通过数量：0
失败数量：1
跳过数量：0
问题定界：tl.extra.cuda.num_threads方法是cuda特有，npu暂无该OP