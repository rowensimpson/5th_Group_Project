from __future__ import print_function
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import tkinter as tk
from matplotlib import style

# Declarations
matplotlib.use("TkAgg")
DIM_Y = [0, 50]
LARGE_FONT = ("Verdana", 12)
style.use('ggplot')

# unit 1 / V and I
a = Figure()
plot_a_0 = a.add_subplot(221)
plot_a_1 = a.add_subplot(222)
plot_a_2 = a.add_subplot(223)
plot_a_3 = a.add_subplot(224)
plot_a_0.set_ylim(DIM_Y)
plot_a_1.set_ylim(DIM_Y)
plot_a_2.set_ylim(DIM_Y)
plot_a_3.set_ylim(DIM_Y)
plot_a_0.set_title("Distribution Voltage", fontsize=10)
plot_a_0.set_xlabel("time(s)", fontsize=7)
plot_a_0.set_ylabel("Voltage(V)", fontsize=7)
plot_a_0.grid(True, linestyle='-', color='0.75')
plot_a_1.set_title("Distribution Current", fontsize=10)
plot_a_1.set_xlabel("time(s)", fontsize=7)
plot_a_1.set_ylabel("Current(I)", fontsize=7)
plot_a_1.grid(True, linestyle='-', color='0.75')
plot_a_2.set_title("Battery Voltage", fontsize=10)
plot_a_2.set_xlabel("time(s)", fontsize=7)
plot_a_2.set_ylabel("Voltage(V)", fontsize=7)
plot_a_2.grid(True, linestyle='-', color='0.75')
plot_a_3.set_title("Battery Current", fontsize=10)
plot_a_3.set_xlabel("time(s)", fontsize=7)
plot_a_3.set_ylabel("Current(I)", fontsize=7)
plot_a_3.grid(True, linestyle='-', color='0.75')
a.tight_layout()
lna_0, = plot_a_0.plot([], [], color='red', lw=2)
lna_1, = plot_a_1.plot([], [], color='blue', lw=2)
lna_2, = plot_a_2.plot([], [], color='red', lw=2)
lna_3, = plot_a_3.plot([], [], color='blue', lw=2)
# unit 2 / V and I plots
b = Figure()
plot_b_0 = b.add_subplot(221)
plot_b_1 = b.add_subplot(222)
plot_b_2 = b.add_subplot(223)
plot_b_3 = b.add_subplot(224)
plot_b_0.set_ylim(DIM_Y)
plot_b_1.set_ylim(DIM_Y)
plot_b_2.set_ylim(DIM_Y)
plot_b_3.set_ylim(DIM_Y)
plot_b_0.set_title("Distribution Voltage", fontsize=10)
plot_b_0.set_xlabel("time(s)", fontsize=7)
plot_b_0.set_ylabel("Voltage(V)", fontsize=7)
plot_b_0.grid(True, linestyle='-', color='0.75')
plot_b_1.set_title("Distribution Current", fontsize=10)
plot_b_1.set_xlabel("time(s)", fontsize=7)
plot_b_1.set_ylabel("Current(I)", fontsize=7)
plot_b_1.grid(True, linestyle='-', color='0.75')
plot_b_2.set_title("Battery Voltage", fontsize=10)
plot_b_2.set_xlabel("time(s)", fontsize=7)
plot_b_2.set_ylabel("Voltage(V)", fontsize=7)
plot_b_2.grid(True, linestyle='-', color='0.75')
plot_b_3.set_title("Battery Current", fontsize=10)
plot_b_3.set_xlabel("time(s)", fontsize=7)
plot_b_3.set_ylabel("Current(I)", fontsize=7)
plot_b_3.grid(True, linestyle='-', color='0.75')
b.tight_layout()
lnb_0, = plot_b_0.plot([], [], color='red', lw=2)
lnb_1, = plot_b_1.plot([], [], color='blue', lw=2)
lnb_2, = plot_b_2.plot([], [], color='red', lw=2)
lnb_3, = plot_b_3.plot([], [], color='blue', lw=2)
# unit 3 / V and I plots
c = Figure()
plot_c_0 = c.add_subplot(221)
plot_c_1 = c.add_subplot(222)
plot_c_2 = c.add_subplot(223)
plot_c_3 = c.add_subplot(224)
plot_c_0.set_ylim(DIM_Y)
plot_c_1.set_ylim(DIM_Y)
plot_c_2.set_ylim(DIM_Y)
plot_c_3.set_ylim(DIM_Y)
plot_c_0.set_title("Distribution Voltage", fontsize=10)
plot_c_0.set_xlabel("time(s)", fontsize=7)
plot_c_0.set_ylabel("Voltage(V)", fontsize=7)
plot_c_0.grid(True, linestyle='-', color='0.75')
plot_c_1.set_title("Distribution Current", fontsize=10)
plot_c_1.set_xlabel("time(s)", fontsize=7)
plot_c_1.set_ylabel("Current(I)", fontsize=7)
plot_c_1.grid(True, linestyle='-', color='0.75')
plot_c_2.set_title("Battery Voltage", fontsize=10)
plot_c_2.set_xlabel("time(s)", fontsize=7)
plot_c_2.set_ylabel("Voltage(V)", fontsize=7)
plot_c_2.grid(True, linestyle='-', color='0.75')
plot_c_3.set_title("Battery Current", fontsize=10)
plot_c_3.set_xlabel("time(s)", fontsize=7)
plot_c_3.set_ylabel("Current(I)", fontsize=7)
plot_c_3.grid(True, linestyle='-', color='0.75')
c.tight_layout()
lnc_0, = plot_c_0.plot([], [], color='red', lw=2)
lnc_1, = plot_c_1.plot([], [], color='blue', lw=2)
lnc_2, = plot_c_2.plot([], [], color='red', lw=2)
lnc_3, = plot_c_3.plot([], [], color='blue', lw=2)


def print_var(ts, dv_1, dc_1, bv_1, bc_1, dv_2, dc_2, bv_2, bc_2, dv_3, dc_3, bv_3, bc_3):

    var_list = [ts, dv_1, dc_1, bv_1, bc_1, dv_2, dc_2, bv_2, bc_2, dv_3, dc_3, bv_3, bc_3]

    for elements in var_list:
        print(elements)


def updateGraphsA(i):
    pullData = open('sampleText.txt', 'r').read()
    dataArray = pullData.split('\n')
    time_stamp = []
    dist_voltage = []
    dist_current = []
    batt_voltage = []
    batt_current = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            ts, dv_1, dc_1, bv_1, bc_1,\
            dv_2, dc_2, bv_2, bc_2,\
            dv_3, dc_3, bv_3, bc_3 = eachLine.split(',')
            time_stamp.append(int(ts))
            dist_voltage.append(int(dv_1))
            dist_current.append(int(dc_1))
            batt_voltage.append(int(bv_1))
            batt_current.append(int(bc_1))
    lna_0.set_xdata(time_stamp)
    lna_0.set_ydata(dist_voltage)
    lna_1.set_xdata(time_stamp)
    lna_1.set_ydata(dist_current)
    lna_2.set_xdata(time_stamp)
    lna_2.set_ydata(batt_voltage)
    lna_3.set_xdata(time_stamp)
    lna_3.set_ydata(batt_current)
    DIM_X = [max(time_stamp)-50, max(time_stamp)+10]
    plot_a_0.set_xlim(DIM_X)
    plot_a_1.set_xlim(DIM_X)
    plot_a_2.set_xlim(DIM_X)
    plot_a_3.set_xlim(DIM_X)
    print('C')


def updateGraphsB(i):
    pullData = open('sampleText.txt', 'r').read()
    dataArray = pullData.split('\n')
    time_stamp = []
    dist_voltage = []
    dist_current = []
    batt_voltage = []
    batt_current = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            ts, dv_1, dc_1, bv_1, bc_1,\
            dv_2, dc_2, bv_2, bc_2,\
            dv_3, dc_3, bv_3, bc_3 = eachLine.split(',')
            time_stamp.append(int(ts))
            dist_voltage.append(int(dv_2))
            dist_current.append(int(dc_2))
            batt_voltage.append(int(bv_2))
            batt_current.append(int(bc_2))
    lnb_0.set_xdata(time_stamp)
    lnb_0.set_ydata(dist_voltage)
    lnb_1.set_xdata(time_stamp)
    lnb_1.set_ydata(dist_current)
    lnb_2.set_xdata(time_stamp)
    lnb_2.set_ydata(batt_voltage)
    lnb_3.set_xdata(time_stamp)
    lnb_3.set_ydata(batt_current)
    DIM_X = [max(time_stamp)-50, max(time_stamp)+10]
    plot_b_0.set_xlim(DIM_X)
    plot_b_1.set_xlim(DIM_X)
    plot_b_2.set_xlim(DIM_X)
    plot_b_3.set_xlim(DIM_X)
    print('C')


def updateGraphsC(i):
    pullData = open('sampleText.txt', 'r').read()
    dataArray = pullData.split('\n')
    time_stamp = []
    dist_voltage = []
    dist_current = []
    batt_voltage = []
    batt_current = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            ts, dv_1, dc_1, bv_1, bc_1,\
            dv_2, dc_2, bv_2, bc_2,\
            dv_3, dc_3, bv_3, bc_3 = eachLine.split(',')
            time_stamp.append(int(ts))
            dist_voltage.append(int(dv_3))
            dist_current.append(int(dc_3))
            batt_voltage.append(int(bv_3))
            batt_current.append(int(bc_3))
    lnc_0.set_xdata(time_stamp)
    lnc_0.set_ydata(dist_voltage)
    lnc_1.set_xdata(time_stamp)
    lnc_1.set_ydata(dist_current)
    lnc_2.set_xdata(time_stamp)
    lnc_2.set_ydata(batt_voltage)
    lnc_3.set_xdata(time_stamp)
    lnc_3.set_ydata(batt_current)
    DIM_X = [max(time_stamp)-50, max(time_stamp)+10]
    plot_c_0.set_xlim(DIM_X)
    plot_c_1.set_xlim(DIM_X)
    plot_c_2.set_xlim(DIM_X)
    plot_c_3.set_xlim(DIM_X)
    print('C')


class TransientAnalysis(tk.Tk):

    def __init__(self, *args, **kwargs):
        self._running_anim = None
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Transient Analysis GUI: v1.0")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GraphPageA, GraphPageB, GraphPageC):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphPageA)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.canvas.draw_idle()


class GraphPageA(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Go to Unit 1", bd=2, bg='green')
        button1.pack(side=tk.TOP)
        button2 = tk.Button(self, text="Go to Unit 2", command=(lambda: controller.show_frame(GraphPageB)))
        button2.pack(side=tk.TOP)
        button3 = tk.Button(self, text="Go to Unit 3", command=(lambda: controller.show_frame(GraphPageC)))
        button3.pack(side=tk.TOP)

        canvasA = FigureCanvasTkAgg(a, self)
        canvasA.show()
        canvasA.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas = canvasA


class GraphPageB(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Go to Unit 1", command=(lambda: controller.show_frame(GraphPageA)))
        button1.pack(side=tk.TOP)
        button2 = tk.Button(self, text="Go to Unit 2", bd=2, bg='green')
        button2.pack(side=tk.TOP)
        button3 = tk.Button(self, text="Go to Unit 3", command=(lambda: controller.show_frame(GraphPageC)))
        button3.pack(side=tk.TOP)

        canvasB = FigureCanvasTkAgg(b, self)
        canvasB.show()
        canvasB.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas = canvasB

class GraphPageC(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="Go to Unit 1", command=(lambda: controller.show_frame(GraphPageA)))
        button1.pack(side=tk.TOP)
        button2 = tk.Button(self, text="Go to Unit 2", command=(lambda: controller.show_frame(GraphPageB)))
        button2.pack(side=tk.TOP)
        button3 = tk.Button(self, text="Go to Unit 3", bd=2, bg='green')
        button3.pack(side=tk.TOP)
        canvasC = FigureCanvasTkAgg(c, self)
        canvasC.show()
        canvasC.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas = canvasC


app = TransientAnalysis()
app.geometry("800x600")
aniA = animation.FuncAnimation(a, updateGraphsA, interval=1000, blit=False)
aniB = animation.FuncAnimation(b, updateGraphsB, interval=1000, blit=False)
aniC = animation.FuncAnimation(c, updateGraphsC, interval=1000, blit=False)
app.mainloop()