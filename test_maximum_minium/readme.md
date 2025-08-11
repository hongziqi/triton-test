## 统计数据

### 运行指令
```bash
pytest -sv language/test_standard.py::test_maximum_minium > test_maximum_minium.log
```

### 统计结果
通过数量：12
失败数量：12
跳过数量：6
问题定界：
TA&BS,
问题归类: 
1. (4个)driver.py 中没有提供'u8'、'u16'类型映射
2. (4个)精度问题(uint32、uint64)
3. (2个)[fp8, fp64]不支持 1
4. (2个)ConvertLinalgRToBinary转换报错：not support bf16 type cast