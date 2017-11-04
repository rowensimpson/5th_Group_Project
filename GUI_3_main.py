from __future__ import print_function
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import tkinter as tk

# Declarations
matplotlib.use("TkAgg")
DIM_Y = [0, 50]
LARGE_FONT = ("Verdana", 12)

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
b = Figure(figsize=(4, 4))
plot_b = b.add_subplot(111)
plot_b.set_xlim([0, 50])
plot_b.set_ylim([0, 50])
lnb, = plot_b.plot([], [], color='olive', lw=2)


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

    print('XXXXXXXXXOOOOOOOOOOOXXXXXXXXXX')
    print(ts, dv_1, dc_1, bv_1, bc_1, dv_2, dc_2, bv_2, bc_2, dv_3, dc_3, bv_3, bc_3)


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

    lnb.set_xdata(dist_voltage)
    lnb.set_ydata(dist_current)


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

        for F in (GraphPageA, GraphPageB):

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
        label = tk.Label(self, text="Unit 1", font=LARGE_FONT).pack(side=tk.TOP)
        button1 = tk.Button(self, text="Show Graph B", command=(lambda: controller.show_frame(GraphPageB)))
        button1.pack(side=tk.TOP)

        canvasA = FigureCanvasTkAgg(a, self)
        canvasA.show()
        canvasA.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas = canvasA



class GraphPageB(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Show Graph A", command=(lambda: controller.show_frame(GraphPageA)))
        button1.pack(side=tk.LEFT)

        canvasB = FigureCanvasTkAgg(b, self)
        canvasB.show()
        #canvasB.get_tk_widget().grid(row=1, column=1, pady=0, padx=0, sticky='nsew')
        canvasB.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas = canvasB



app = TransientAnalysis()
app.geometry("800x600")
aniA = animation.FuncAnimation(a, updateGraphsA, interval=1000, blit=False)
aniB = animation.FuncAnimation(b, updateGraphsB, interval=1000, blit=False)
app.mainloop()