wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-500M'
n_layer = 36
n_head = 16
n_embd = 1024

batch_size = 20
block_size = 1024
gradient_accumulation_steps = 3

max_iters = 600000
lr_decay_iters = 600000

# eval stuff
eval_interval = 1000
eval_iters = 200
log_interval = 10

# weight decay
weight_decay = 1e-1
