## 统计数据

### 运行指令
```bash
pytest -sv language/test_core.py::test_empty_kernel > test_empty_kernel.log
```

### 统计结果
通过数量：10
失败数量：2
跳过数量：0
问题定界：TA, driver.py 中没有提供'u8'、'u16'的类型映射（涉及函数convert_sigtype_to_int）
