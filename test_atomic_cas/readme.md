## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_atomic_cas > test_atomic_cas.log
```

### 统计结果
通过数量：0
失败数量：5
跳过数量：0
问题定界：TA, BS, MLIRCompilationError（ConvertLinalgRToBinary 转换为二进制文件报错）