import gym

env = gym.make('CartPole-v1')
observation = env.reset()

Kp = 10;
Kd = 12;
Ki = 4;
F = 0
integral = 0
force = 0;

for _ in range(1000):
    env.render()
    observation, reward, done , info = env.step(force)
    theta = observation[2]
    angular_vel = observation[3]

    integral += theta
    F = Kp*theta + Ki*integral + Kd*angular_vel

    if F > 0:
        force = 1
    else:
        force = 0

    print(force)        

    if done:
        observation = env.reset()
        integral = 0

env.close()