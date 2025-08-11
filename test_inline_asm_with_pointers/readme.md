## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_inline_asm_with_pointers > test_inline_asm_with_pointers.log
```

### 统计结果
通过数量：0
失败数量：1
跳过数量：0
问题定界：TA, ConvertTritonIRToLinalgIR 转换异常导致