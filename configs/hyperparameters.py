## Architechture
lpips_type = 'alex'
first_inv_type = 'w'
optim_type = 'adam'

## Locality regularization
latent_ball_num_of_samples = 100
locality_regularization_interval = 100
use_locality_regularization = True
regulizer_l2_lambda = 500
regulizer_lpips_lambda = 500
regulizer_alpha = 3000

## Loss
pt_l2_lambda = 1
pt_lpips_lambda = 1

## Steps
LPIPS_value_threshold = 0.06
max_pti_steps = 800
first_inv_steps = 800
max_images_to_invert = 30

## Optimization
pti_learning_rate = 3e-4
first_inv_lr = 5e-3
train_batch_size = 1
use_last_w_pivots = False
