import gym
env = gym.make('Pendulum-v0')
print(env.action_space)
print(env.action_space.high)
print(env.action_space.low)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
raw_input("Press Any Key to continue...")
for i_episode in range(20):
	observation = env.reset()
	for t in range(1000):
		env.render()
		print('observation')
		print(observation)
		#action = env.action_space.sample()
		action = 0
		observation, reward, done, info = env.step(action)
		print('reward')
		print(reward)
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			break