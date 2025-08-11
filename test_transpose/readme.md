## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_transpose > test_transpose.log
```

### 统计结果
通过数量：0
失败数量：12
跳过数量：0
问题定界：TA, 11个问题：MLIRCompilationError（ConvertTritonIRToLinalgIR 转换异常导致）；1个问题：[fp8, fp64]不支持