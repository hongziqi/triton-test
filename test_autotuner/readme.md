## 统计数据

### 运行指令
```bash
pytest -sv runtime/test_autotuner.py > test_autotuner.log
```

### 统计结果
通过数量：0
失败数量：6
跳过数量：0
问题定界：
TA
问题归类:
1.（6个）NPU 后端注入元参数，但内核函数签名未用`**kwargs`接收，被`inspect`严格检查拦截。（测试样例中，内核函数添加 `**META`可跑通）
2. （1个）非问题，`use_cuda_graph` 是 CUDA 特有，NPU报错。