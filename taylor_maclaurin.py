#~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~
#This contains the entire code used to generate this video
#date: 21/02/2021
#author: Samuel Khongthaw
#~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~
from manim import*
import numpy as np
class Taylor(GraphScene,ZoomedScene):
	#initialization of the inherited classes
	def __init__(self, **kwargs):
		GraphScene.__init__(self,
			x_axis_label = "$x$",
			y_axis_label = "$y$",
			x_min = -6,
			x_max = 6,
			y_min = -4,
			y_max = 4,
			graph_origin = 1.5*DOWN+0.4*RIGHT,
			axes_color = WHITE)
		GraphScene.setup(self)
		ZoomedScene.setup(self)
	def construct(self):
			#intro
		quote = Tex("If you love something, you want to show it to the world.")
		self.play(FadeIn(quote))
		self.wait(2)
		self.play(FadeOut(quote))
			#splash
		thenose = Tex("99 luftballoons")
		circle = Circle()
		circle2 = Circle()
		circle3 = Circle()
		circle4 = Circle()
		circle5 = Circle()
		circle5.shift(RIGHT)
		circle4.shift(LEFT)
		circle3.shift(DOWN)
		circle2.shift(UP)
		circle.set_stroke(color = RED, width = 5)
		self.play(ShowCreation(circle))
		self.play(ShowCreation(circle2))
		self.play(ShowCreation(circle3))
		self.play(ShowCreation(circle4),ShowCreation(circle5))
		thenose.shift(2.5*DOWN)
		self.play(FadeIn(thenose))
		self.wait(2)
		self.play(FadeOut(circle),FadeOut(circle2),FadeOut(circle3),FadeOut(circle4),FadeOut(circle5),FadeOut(thenose))
		self.wait(1)
			#goal of the video
		goal = Tex("How does the process of"," approximating ","functions using the ","Taylor / Maclaurin series ","actually look like?").scale(0.8)			
		goal.set_color_by_tex("approximating",RED)
		goal.set_color_by_tex("Taylor / Maclaurin series",RED)
		self.play(Write(goal))
		self.wait(3)
		self.play(FadeOut(goal))
			#fucntion to be approximated
		def function(x):
			return np.exp(x)
			#maclaurin series polynomial
		Equation = MathTex("g(x)=","\\frac{f^{(0)}(0)}{0!}","+","\\frac{f^{(1)}(0)}{1!}","x","+","\\frac{f^{(2)}(0)}{2!}","x^2","+","\\frac{f^{(3)}(0)}{3!}","x^3","+","\\frac{f^{(4)}(0)}{4!}","x^4","+","\\frac{f^{(5)}(0)}{5!}","x^5","...")
		text = Tex("The Taylor / Maclaurin Series")
		text.next_to(Equation,1.5*DOWN)
		Equation.scale(0.8)
		colors = ["#7cd5e7","#874db8",YELLOW,"#b853cc","#6253c3",GREEN] #colors to be used
		j , Derivative_pos = 0,[1,3,6,9,12,15]
			#loop to set the colors of the derivative terms of the Equation MObject
		for i in colors:
			Equation[Derivative_pos[j]].set_color(i)
			j += 1
		self.play(DrawBorderThenFill(Equation))
		self.play(FadeInFrom(text,UP))
		self.wait(3)
		self.play(ApplyMethod(Equation.shift,3.5*UP),FadeOut(text))
			#setting up the graph on the scene
		self.setup_axes(animate = True)
		    #Writing the function to be plotted on the scene
		func = MathTex("f(x)=e^x").shift(3*LEFT,2*UP)
		func.set_color(RED)
		self.play(Write(func)) 
		graph = self.get_graph(function)
		graph.set_color(RED)
		self.play(ShowCreation(graph), run_time = 3)
		self.wait(2)
		#setting up the zoom camera
		self.zoomed_camera.frame.scale(3)
		zoomed_display = self.zoomed_display
		zoomed_display.shift(DOWN)
		self.activate_zooming(animate = True)
		self.play(ApplyMethod(self.zoomed_camera.frame.shift,.75*DOWN+.3*RIGHT))
		#approximations of the fucntion
		def approx1(x):
			return(1)
		def approx2(x):
			return(approx1(x) + x)
		def approx3(x):
			return(approx2(x)+(x**2)/2)
		def approx4(x):
			return(approx3(x)+(x**3)/6)
		def approx5(x):
			return(approx4(x)+(x**4)/24)
		def approx6(x):
			return(approx5(x)+(x**5)/120)
		
		constants = [MathTex("1").set_color(colors[0]).move_to(Equation[1]),MathTex("1").set_color(colors[1]).move_to(Equation[3]),MathTex("\\frac{1}{2}").set_color(colors[2]).move_to(Equation[6]),MathTex("\\frac{1}{6}").set_color(colors[3]).move_to(Equation[9]),MathTex("\\frac{1}{24}").set_color(colors[4]).move_to(Equation[12]),MathTex("\\frac{1}{120}").set_color(colors[5]).move_to(Equation[15])]
		derivatives = [MathTex("\\frac{f^{(0)}(0)}{0!}=1").set_color(colors[0]).next_to(func,DOWN),MathTex("\\frac{f^{(1)}(0)}{1!}=1").set_color(colors[1]).next_to(func,DOWN),MathTex("\\frac{f^{(2)}(0)}{2!}=\\frac{1}{2}").set_color(colors[2]).next_to(func,DOWN),MathTex("\\frac{f^{(3)}(0)}{3!}=\\frac{1}{6}").set_color(colors[3]).next_to(func,DOWN),MathTex("\\frac{f^{(4)}(0)}{4!}=\\frac{1}{24}").set_color(colors[4]).next_to(func,DOWN),MathTex("\\frac{f^{(5)}(0)}{5!}=\\frac{1}{120}").set_color(colors[5]).next_to(func,DOWN)]
		brace1 = Brace(Equation[0:2])
		brace2 = Brace(Equation[0:5])
		brace3 = Brace(Equation[0:8])
		brace4 = Brace(Equation[0:11])
		brace5 = Brace(Equation[0:14])
		brace6 = Brace(Equation[0:17])
		#First approximation
		self.play(GrowFromCenter(derivatives[0]))
		self.play(FadeOut(Equation[1]),ReplacementTransform(derivatives[0],constants[0]),run_time = 2)
		approx1_graph = self.get_graph(approx1).set_color(colors[0])
		self.play(GrowFromCenter(brace1),ShowCreation(approx1_graph),run_time = 3)
		#Second approximation
		self.play(GrowFromCenter(derivatives[1]))
		self.play(FadeOut(Equation[3]),ReplacementTransform(derivatives[1],constants[1]),run_time = 2)
		approx2_graph = self.get_graph(approx2).set_color(colors[1])
		self.play(ReplacementTransform(brace1,brace2),ReplacementTransform(approx1_graph,approx2_graph),run_time = 2.5)
		#Third approximation
		self.play(GrowFromCenter(derivatives[2]))
		self.play(FadeOut(Equation[6]),ReplacementTransform(derivatives[2],constants[2]),run_time = 2)
		approx3_graph = self.get_graph(approx3).set_color(colors[2])
		self.play(ReplacementTransform(brace2,brace3),ReplacementTransform(approx2_graph,approx3_graph),run_time = 2.5)
		#Fourth approximation
		self.play(GrowFromCenter(derivatives[3]))
		self.play(FadeOut(Equation[9]),ReplacementTransform(derivatives[3],constants[3]),run_time = 2)
		approx4_graph = self.get_graph(approx4).set_color(colors[3])
		self.play(ReplacementTransform(brace3,brace4),ReplacementTransform(approx3_graph,approx4_graph),run_time = 2.5)
		#Fifth approximation
		self.play(GrowFromCenter(derivatives[4]))
		self.play(FadeOut(Equation[12]),ReplacementTransform(derivatives[4],constants[4]),run_time = 2)
		approx5_graph = self.get_graph(approx5).set_color(colors[4])
		self.play(ReplacementTransform(brace4,brace5),ReplacementTransform(approx4_graph,approx5_graph),run_time = 2.5)
		#Sixth approximation
		self.play(GrowFromCenter(derivatives[5]))
		self.play(FadeOut(Equation[15]),ReplacementTransform(derivatives[5],constants[5]),run_time = 2)
		approx6_graph = self.get_graph(approx6).set_color(colors[5])
		self.play(ReplacementTransform(brace5,brace6),ReplacementTransform(approx5_graph,approx6_graph),run_time = 2.5)
		self.wait(2)
		self.remove(Equation)
		self.play(FadeOut(graph),FadeOut(approx6_graph),FadeOut(brace6),FadeOut(func),FadeOut(constants[0]),FadeOut(constants[1]),FadeOut(constants[2]),FadeOut(constants[3]),FadeOut(constants[4]),FadeOut(constants[5]))
		self.play(Write(Equation))
		self.wait(1)
		#Second graph
		def function(x):
			return np.sin(x)
		    #Writing the function to be plotted on the scene
		func = MathTex("f(x)=sin(x)").shift(3*LEFT,2*UP)
		func.set_color(RED)
		self.play(Write(func)) 
		graph = self.get_graph(function)
		graph.set_color(RED)
		self.play(ShowCreation(graph), run_time = 3)
		self.wait(2)
		#move the camera frame
		self.play(ApplyMethod(self.zoomed_camera.frame.shift,0.7*DOWN))
		#approximations of the fucntion
		def approx1(x):
			return(0)
		def approx2(x):
			return(approx1(x) + x)
		def approx3(x):
			return(approx2(x)+0)
		def approx4(x):
			return(approx3(x)-(x**3)/6)
		def approx5(x):
			return(approx4(x)+0)
		def approx6(x):
			return(approx5(x)+(x**5)/120)
		
		constants = [MathTex("0").set_color(colors[0]).move_to(Equation[1]),MathTex("1").set_color(colors[1]).move_to(Equation[3]),MathTex("0").set_color(colors[2]).move_to(Equation[6]),MathTex("(-\\frac{1}{6})").set_color(colors[3]).move_to(Equation[9]),MathTex("0").set_color(colors[4]).move_to(Equation[12]),MathTex("\\frac{1}{120}").set_color(colors[5]).move_to(Equation[15])]
		derivatives = [MathTex("\\frac{f^{(0)}(0)}{0!}=0").set_color(colors[0]).next_to(func,DOWN),MathTex("\\frac{f^{(1)}(0)}{1!}=1").set_color(colors[1]).next_to(func,DOWN),MathTex("\\frac{f^{(2)}(0)}{2!}=0").set_color(colors[2]).next_to(func,DOWN),MathTex("\\frac{f^{(3)}(0)}{3!}=-\\frac{1}{6}").set_color(colors[3]).next_to(func,DOWN),MathTex("\\frac{f^{(4)}(0)}{4!}=0").set_color(colors[4]).next_to(func,DOWN),MathTex("\\frac{f^{(5)}(0)}{5!}=\\frac{1}{120}").set_color(colors[5]).next_to(func,DOWN)]
		brace1 = Brace(Equation[0:2])
		brace2 = Brace(Equation[0:5])
		brace3 = Brace(Equation[0:8])
		brace4 = Brace(Equation[0:11])
		brace5 = Brace(Equation[0:14])
		brace6 = Brace(Equation[0:17])
		#First approximation
		self.play(GrowFromCenter(derivatives[0]))
		self.play(FadeOut(Equation[1]),ReplacementTransform(derivatives[0],constants[0]),run_time = 2)
		approx1_graph = self.get_graph(approx1).set_color(colors[0])
		self.play(GrowFromCenter(brace1),ShowCreation(approx1_graph),run_time = 3)
		#Second approximation
		self.play(GrowFromCenter(derivatives[1]))
		self.play(FadeOut(Equation[3]),ReplacementTransform(derivatives[1],constants[1]),run_time = 2)
		approx2_graph = self.get_graph(approx2).set_color(colors[1])
		self.play(ReplacementTransform(brace1,brace2),ReplacementTransform(approx1_graph,approx2_graph),run_time = 2.5)
		#Third approximation
		self.play(GrowFromCenter(derivatives[2]))
		self.play(FadeOut(Equation[6]),ReplacementTransform(derivatives[2],constants[2]),run_time = 2)
		approx3_graph = self.get_graph(approx3).set_color(colors[2])
		self.play(ReplacementTransform(brace2,brace3),ReplacementTransform(approx2_graph,approx3_graph),run_time = 2.5)
		#Fourth approximation
		self.play(GrowFromCenter(derivatives[3]))
		self.play(FadeOut(Equation[9]),ReplacementTransform(derivatives[3],constants[3]),run_time = 2)
		approx4_graph = self.get_graph(approx4).set_color(colors[3])
		self.play(ReplacementTransform(brace3,brace4),ReplacementTransform(approx3_graph,approx4_graph),run_time = 2.5)
		#Fifth approximation
		self.play(GrowFromCenter(derivatives[4]))
		self.play(FadeOut(Equation[12]),ReplacementTransform(derivatives[4],constants[4]),run_time = 2)
		approx5_graph = self.get_graph(approx5).set_color(colors[4])
		self.play(ReplacementTransform(brace4,brace5),ReplacementTransform(approx4_graph,approx5_graph),run_time = 2.5)
		#Sixth approximation
		self.play(GrowFromCenter(derivatives[5]))
		self.play(FadeOut(Equation[15]),ReplacementTransform(derivatives[5],constants[5]),run_time = 2)
		approx6_graph = self.get_graph(approx6).set_color(colors[5])
		self.play(ReplacementTransform(brace5,brace6),ReplacementTransform(approx5_graph,approx6_graph),run_time = 2.5)
		self.wait(2)
		self.remove(Equation)
		self.play(FadeOut(graph),FadeOut(approx6_graph),FadeOut(brace6),FadeOut(func),FadeOut(constants[0]),FadeOut(constants[1]),FadeOut(constants[2]),FadeOut(constants[3]),FadeOut(constants[4]),FadeOut(constants[5]))
		self.play(Write(Equation))
		self.wait(1)
		#Third graph
		def function(x):
			return np.log(1+x)
 #Writing the function to be plotted on the scene
		func = MathTex("f(x)=ln(1+x)").shift(3*LEFT,2*UP)
		func.set_color(RED)
		self.play(Write(func)) 
		graph = self.get_graph(function,x_min=-.8,x_max = 6)
		graph.set_color(RED)
		self.play(ShowCreation(graph), run_time = 3)
		self.wait(2)
		#approximations of the fucntion
		def approx1(x):
			return(0)
		def approx2(x):
			return(approx1(x) + x)
		def approx3(x):
			return(approx2(x)- (x**2)/2)
		def approx4(x):
			return(approx3(x)+((x**3)/3))
		def approx5(x):
			return(approx4(x)-((x**4)/4))
		def approx6(x):
			return(approx5(x)+((x**5)/5))
		
		constants = [MathTex("0").set_color(colors[0]).move_to(Equation[1]),MathTex("1").set_color(colors[1]).move_to(Equation[3]),MathTex("(-\\frac{1}{2})").set_color(colors[2]).move_to(Equation[6]),MathTex("\\frac{1}{3}").set_color(colors[3]).move_to(Equation[9]),MathTex("(-\\frac{1}{4})").set_color(colors[4]).move_to(Equation[12]),MathTex("\\frac{1}{5}").set_color(colors[5]).move_to(Equation[15])]
		derivatives = [MathTex("\\frac{f^{(0)}(0)}{0!}=0").set_color(colors[0]).next_to(func,DOWN),MathTex("\\frac{f^{(1)}(0)}{1!}=1").set_color(colors[1]).next_to(func,DOWN),MathTex("\\frac{f^{(2)}(0)}{2!}=-\\frac{1}{2}").set_color(colors[2]).next_to(func,DOWN),MathTex("\\frac{f^{(3)}(0)}{3!}=\\frac{1}{3}").set_color(colors[3]).next_to(func,DOWN),MathTex("\\frac{f^{(4)}(0)}{4!}=(-\\frac{1}{4})").set_color(colors[4]).next_to(func,DOWN),MathTex("\\frac{f^{(5)}(0)}{5!}=\\frac{1}{5}").set_color(colors[5]).next_to(func,DOWN)]
		brace1 = Brace(Equation[0:2])
		brace2 = Brace(Equation[0:5])
		brace3 = Brace(Equation[0:8])
		brace4 = Brace(Equation[0:11])
		brace5 = Brace(Equation[0:14])
		brace6 = Brace(Equation[0:17])
		#First approximation
		self.play(GrowFromCenter(derivatives[0]))
		self.play(FadeOut(Equation[1]),ReplacementTransform(derivatives[0],constants[0]),run_time = 2)
		approx1_graph = self.get_graph(approx1).set_color(colors[0])
		self.play(GrowFromCenter(brace1),ShowCreation(approx1_graph),run_time = 3)
		#Second approximation
		self.play(GrowFromCenter(derivatives[1]))
		self.play(FadeOut(Equation[3]),ReplacementTransform(derivatives[1],constants[1]),run_time = 2)
		approx2_graph = self.get_graph(approx2).set_color(colors[1])
		self.play(ReplacementTransform(brace1,brace2),ReplacementTransform(approx1_graph,approx2_graph),run_time = 2.5)
		#Third approximation
		self.play(GrowFromCenter(derivatives[2]))
		self.play(FadeOut(Equation[6]),ReplacementTransform(derivatives[2],constants[2]),run_time = 2)
		approx3_graph = self.get_graph(approx3).set_color(colors[2])
		self.play(ReplacementTransform(brace2,brace3),ReplacementTransform(approx2_graph,approx3_graph),run_time = 2.5)
		#Fourth approximation
		self.play(GrowFromCenter(derivatives[3]))
		self.play(FadeOut(Equation[9]),ReplacementTransform(derivatives[3],constants[3]),run_time = 2)
		approx4_graph = self.get_graph(approx4).set_color(colors[3])
		self.play(ReplacementTransform(brace3,brace4),ReplacementTransform(approx3_graph,approx4_graph),run_time = 2.5)
		#Fifth approximation
		self.play(GrowFromCenter(derivatives[4]))
		self.play(FadeOut(Equation[12]),ReplacementTransform(derivatives[4],constants[4]),run_time = 2)
		approx5_graph = self.get_graph(approx5).set_color(colors[4])
		self.play(ReplacementTransform(brace4,brace5),ReplacementTransform(approx4_graph,approx5_graph),run_time = 2.5)
		#Sixth approximation
		self.play(GrowFromCenter(derivatives[5]))
		self.play(FadeOut(Equation[15]),ReplacementTransform(derivatives[5],constants[5]),run_time = 2)
		approx6_graph = self.get_graph(approx6).set_color(colors[5])
		self.play(ReplacementTransform(brace5,brace6),ReplacementTransform(approx5_graph,approx6_graph),run_time = 2.5)
		self.wait(2)
		self.remove(Equation)
		self.play(FadeOut(graph),FadeOut(approx6_graph),FadeOut(brace6),FadeOut(func),FadeOut(constants[0]),FadeOut(constants[1]),FadeOut(constants[2]),FadeOut(constants[3]),FadeOut(constants[4]),FadeOut(constants[5]))
		self.play(Write(Equation))
		self.wait(1)
		#Fourth Graph
		def function(x):
			return x**4-3*x**2+1
			#maclaurin series polynomial
				    #Writing the function to be plotted on the scene
		func = MathTex("f(x)=x^4-3x^2+1").shift(3.3*LEFT,2*UP)
		func.set_color(RED)
		self.play(Write(func)) 
		graph = self.get_graph(function)
		graph.set_color(RED)
		self.play(ShowCreation(graph), run_time = 3)
		self.wait(2)
		#move the camera frame
		self.play(ApplyMethod(self.zoomed_camera.frame.shift,0.2*UP))
		#approximations of the fucntion
		def approx1(x):
			return(1)
		def approx2(x):
			return(approx1(x) + 0)
		def approx3(x):
			return(approx2(x)- 3*(x**2))
		def approx4(x):
			return(approx3(x) + 0)
		def approx5(x):
			return(approx4(x)+(x**4))
		def approx6(x):
			return(approx5(x)+0)
		
		constants = [MathTex("1").set_color(colors[0]).move_to(Equation[1]),MathTex("0").set_color(colors[1]).move_to(Equation[3]),MathTex("(-3)").set_color(colors[2]).move_to(Equation[6]),MathTex("0").set_color(colors[3]).move_to(Equation[9]),MathTex("1").set_color(colors[4]).move_to(Equation[12]),MathTex("0").set_color(colors[5]).move_to(Equation[15])]
		derivatives = [MathTex("\\frac{f^{(0)}(0)}{0!}=1").set_color(colors[0]).next_to(func,DOWN),MathTex("\\frac{f^{(1)}(0)}{1!}=0").set_color(colors[1]).next_to(func,DOWN),MathTex("\\frac{f^{(2)}(0)}{2!}=-3").set_color(colors[2]).next_to(func,DOWN),MathTex("\\frac{f^{(3)}(0)}{3!}=0").set_color(colors[3]).next_to(func,DOWN),MathTex("\\frac{f^{(4)}(0)}{4!}=1").set_color(colors[4]).next_to(func,DOWN),MathTex("\\frac{f^{(5)}(0)}{5!}=0").set_color(colors[5]).next_to(func,DOWN)]
		brace1 = Brace(Equation[0:2])
		brace2 = Brace(Equation[0:5])
		brace3 = Brace(Equation[0:8])
		brace4 = Brace(Equation[0:11])
		brace5 = Brace(Equation[0:14])
		brace6 = Brace(Equation[0:17])
		#First approximation
		self.play(GrowFromCenter(derivatives[0]))
		self.play(FadeOut(Equation[1]),ReplacementTransform(derivatives[0],constants[0]),run_time = 2)
		approx1_graph = self.get_graph(approx1).set_color(colors[0])
		self.play(GrowFromCenter(brace1),ShowCreation(approx1_graph),run_time = 3)
		#Second approximation
		self.play(GrowFromCenter(derivatives[1]))
		self.play(FadeOut(Equation[3]),ReplacementTransform(derivatives[1],constants[1]),run_time = 2)
		approx2_graph = self.get_graph(approx2).set_color(colors[1])
		self.play(ReplacementTransform(brace1,brace2),ReplacementTransform(approx1_graph,approx2_graph),run_time = 2.5)
		#Third approximation
		self.play(GrowFromCenter(derivatives[2]))
		self.play(FadeOut(Equation[6]),ReplacementTransform(derivatives[2],constants[2]),run_time = 2)
		approx3_graph = self.get_graph(approx3).set_color(colors[2])
		self.play(ReplacementTransform(brace2,brace3),ReplacementTransform(approx2_graph,approx3_graph),run_time = 2.5)
		#Fourth approximation
		self.play(GrowFromCenter(derivatives[3]))
		self.play(FadeOut(Equation[9]),ReplacementTransform(derivatives[3],constants[3]),run_time = 2)
		approx4_graph = self.get_graph(approx4).set_color(colors[3])
		self.play(ReplacementTransform(brace3,brace4),ReplacementTransform(approx3_graph,approx4_graph),run_time = 2.5)
		#Fifth approximation
		self.play(GrowFromCenter(derivatives[4]))
		self.play(FadeOut(Equation[12]),ReplacementTransform(derivatives[4],constants[4]),run_time = 2)
		approx5_graph = self.get_graph(approx5).set_color(colors[4])
		self.play(ReplacementTransform(brace4,brace5),ReplacementTransform(approx4_graph,approx5_graph),run_time = 2.5)
		#Sixth approximation
		self.play(GrowFromCenter(derivatives[5]))
		self.play(FadeOut(Equation[15]),ReplacementTransform(derivatives[5],constants[5]),run_time = 2)
		approx6_graph = self.get_graph(approx6).set_color(colors[5])
		self.play(ReplacementTransform(brace5,brace6),ReplacementTransform(approx5_graph,approx6_graph),run_time = 2.5)
		self.wait(2)
		self.remove(Equation)
		self.play(FadeOut(Equation),FadeOut(graph),FadeOut(approx6_graph),FadeOut(brace6),FadeOut(func),FadeOut(constants[0]),FadeOut(constants[1]),FadeOut(constants[2]),FadeOut(constants[3]),FadeOut(constants[4]),FadeOut(constants[5]))
		self.wait(1)
