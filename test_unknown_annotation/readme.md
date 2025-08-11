## 统计数据

### 运行指令
```bash
pytest -sv language/test_annotations.py::test_unknown_annotation > test_unknown_annotation.log
```

### 统计结果
通过数量：0
失败数量：1
跳过数量：0
问题定界：TA, 闯入错误的类型的时候应该报错AttributeError，而不是直接编译失败
