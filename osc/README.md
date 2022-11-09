# Instruction to serve BLOOM on osc ascend server
1. Build the container image.

```
singularity build bloom.sif Singularity.def.
```

2. Change paths in `start_server.X.job` to point to the cloned workspace and built image.

3. Submit the job `qsub start_server.X.job`.

4. Once the job is running, check the output and look for server address like `10.x.x.x`. Tunneling the port back to somewhere you have access. 

5. Follow example in `inference_server/examples/server_request.py` to send http requests and get outptus.