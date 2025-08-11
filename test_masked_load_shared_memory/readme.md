## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_masked_load_shared_memory > test_masked_load_shared_memory.log
```

### 统计结果
通过数量：0
失败数量：3
跳过数量：0
问题定界：TA, MLIRCompilationError（ConvertTritonIRToLinalgIR 转换异常导致）