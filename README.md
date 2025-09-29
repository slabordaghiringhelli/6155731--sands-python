I imported matplotlib and numpy in order to be able to use other functions or expressions such as the sine function and to be able to plot said functions. Furthermore, by importing numpy I also could use the pi value.
Then, I defined the function create_sine_wave with the keyword def. 
Afterwards, I defined the parameters t and y, where t is a time array defined using np.linspace.
The variable t was defined from 0 to the duration with a standard sampling rate of 44.1 kHz. 
The variable y is defined as y=sin(2πft), which is also an array as it contains t.
I entered the keyword return followed by t,y.
Then I entered t,y = create_sine_wave(1,2) and then I plotted the sine graph by using plt.plot(t,y).I used plt.xlabel(), plt.ylabel() and plt.title() to add more information to my graph.
