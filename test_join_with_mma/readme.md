## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_join_with_mma > test_join_with_mma.log
```

### 统计结果
通过数量：0
失败数量：1
跳过数量：0
问题定界：BS, MLIRCompilationError（ConvertLinalgRToBinary 转换为二进制文件报错）