from __future__ import print_function
from tkinter import *
import tkinter as tk

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import multiprocessing

import transmitter
import statemodule

if __name__ == '__main__':

    # Declarations
    matplotlib.use("TkAgg")
    DIM_Y = [0, 50]
    ranger = 80
    LARGE_FONT = ("Verdana", 12)
    style.use('ggplot')
    RANGE = 70
    WIDTH = 20
    OFFSET = 12


    # init queues between the processes
    process1in = multiprocessing.Queue()

    # unit 1 / V and I
    a = Figure(figsize=(10, 5), dpi=100)
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
    b = Figure(figsize=(10, 5), dpi=100)
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
    c = Figure(figsize=(10, 5), dpi=100)
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

    # this function collects and graphs Unit 1 Data
    def updateGraphsA(i):

        global ranger

        pullData = open('UnitData.txt', 'r').read()
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
        DIM_X = [max(time_stamp)-ranger, max(time_stamp)+10]
        plot_a_0.set_xlim(DIM_X)
        plot_a_1.set_xlim(DIM_X)
        plot_a_2.set_xlim(DIM_X)
        plot_a_3.set_xlim(DIM_X)

    # this function collects and graphs Unit 2 Data
    def updateGraphsB(i):

        global ranger

        pullData = open('UnitData.txt', 'r').read()
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
        DIM_X = [max(time_stamp)-ranger, max(time_stamp)+10]
        plot_b_0.set_xlim(DIM_X)
        plot_b_1.set_xlim(DIM_X)
        plot_b_2.set_xlim(DIM_X)
        plot_b_3.set_xlim(DIM_X)

    # this function collects and graphs Unit 3 Data
    def updateGraphsC(i):

        global ranger

        pullData = open('UnitData.txt', 'r').read()
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
        DIM_X = [max(time_stamp)-ranger, max(time_stamp)+10]
        plot_c_0.set_xlim(DIM_X)
        plot_c_1.set_xlim(DIM_X)
        plot_c_2.set_xlim(DIM_X)
        plot_c_3.set_xlim(DIM_X)

    # this function sends state change commands
    def state_exe():
        global process1in
        process1in.put(stateOut.get_state_list())

    # this function controls the state selection buttons before execution stage
    def state_control_function(B1_marker, B2_marker, B3_marker, B4_marker, B5_marker, B6_marker, B7_marker, B8_marker, B9_marker):

        if B1_marker:
            stateOut.set_unit1('importing')
        if B2_marker:
            stateOut.set_unit1('exporting')
        if B3_marker:
            stateOut.set_unit1('reset')
        if B4_marker:
            stateOut.set_unit2('importing')
        if B5_marker:
            stateOut.set_unit2('exporting')
        if B6_marker:
            stateOut.set_unit2('reset')
        if B7_marker:
            stateOut.set_unit3('importing')
        if B8_marker:
            stateOut.set_unit3('exporting')
        if B9_marker:
            stateOut.set_unit3('reset')

    #  starts process1 and process2, both communications processes
    def worker_init():
        global process1in
        proc1 = multiprocessing.Process(target=transmitter.transceiver, args=(process1in,))
        proc1.start()

    # kills all periferal processes
    def poison_pill():
        global process1in
        process1in.put(None)

    # state update function
    def state_update():
        global unit1Label
        global unit2Label
        global unit3Label

        pullData = open('state.txt', 'r').read()
        if len(pullData) > 1:
            Unit1_State_in, Unit2_State_in, Unit3_State_in = pullData.split(',')
            Unit3_State_in = Unit3_State_in.strip()
            stateIn.set_unit1(Unit1_State_in)
            stateIn.set_unit2(Unit2_State_in)
            stateIn.set_unit3(Unit3_State_in)
            unit1Label.set(stateIn.get_unit1())
            unit2Label.set(stateIn.get_unit2())
            unit3Label.set(stateIn.get_unit3())

        app.after(5000, state_update)

    # control for the graph scale
    def ranging_function(offset):
        global ranger
        ranger = offset

    # GUI frame control
    class HUGGUI(tk.Tk):

        def __init__(self, *args, **kwargs):
            self._running_anim = None
            tk.Tk.__init__(self, *args, **kwargs)
            tk.Tk.wm_title(self, "HUG systems")

            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (StateHandler, GraphPageA, GraphPageB, GraphPageC):

                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StateHandler)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()
            if cont != StateHandler:
                frame.canvas.draw_idle()

    # Unit 1 data page
    class GraphPageA(tk.Frame):


        def __init__(self, parent, controller):

            global unit1Label
            tk.Frame.__init__(self, parent)
            button1 = tk.Button(self, text="Go to Unit 1", bd=2, bg='green')
            button1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
            button2 = tk.Button(self, text="Go to Unit 2", width=WIDTH, command=(lambda: controller.show_frame(GraphPageB)))
            button2.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
            button3 = tk.Button(self, text="Go to Unit 3", width=WIDTH, command=(lambda: controller.show_frame(GraphPageC)))
            button3.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
            button4 = tk.Button(self, text="State Control", width=WIDTH, command=(lambda: controller.show_frame(StateHandler)))
            button4.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
            slider = tk.Scale(self, from_=10, to=200, orient=HORIZONTAL, bg="lightblue")
            slider.grid(row=0, column=2, sticky='nsew')
            button5 = tk.Button(self, text="Scale", width=WIDTH, bg="lightblue", command=(lambda: ranging_function(slider.get())))
            button5.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

            unit1Label = StringVar()
            unit1Label.set('helloworld')
            label1 = Label(self, text="Unit 1 State:", bg="lightblue").grid(row=0, column=3, sticky='nsew')
            label2 = Label(self, textvariable=unit1Label, bg="lightblue", font=30).grid(row=1, column=3, sticky='nsew')

            canvasA = FigureCanvasTkAgg(a, self)
            canvasA.show()
            canvasA.get_tk_widget().grid(row=2, column=0, columnspan=4)
            self.canvas = canvasA

    # Unit 2 data page
    class GraphPageB(tk.Frame):

        def __init__(self, parent, controller):
            global unit2Label
            tk.Frame.__init__(self, parent)
            button1 = tk.Button(self, text="Go to Unit 1", width=WIDTH, command=(lambda: controller.show_frame(GraphPageA)))
            button1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
            button2 = tk.Button(self, text="Go to Unit 2", width=WIDTH, bd=2, bg='green')
            button2.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
            button3 = tk.Button(self, text="Go to Unit 3", width=WIDTH, command=(lambda: controller.show_frame(GraphPageC)))
            button3.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
            button4 = tk.Button(self, text="State Control", width=WIDTH, command=(lambda: controller.show_frame(StateHandler)))
            button4.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
            slider = tk.Scale(self, from_=10, to=200, orient=HORIZONTAL, bg="lightblue")
            slider.grid(row=0, column=2, sticky='nsew')
            button5 = tk.Button(self, text="Scale", width=WIDTH, bg="lightblue", command=(lambda: ranging_function(slider.get())))
            button5.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

            unit2Label = StringVar()
            unit2Label.set('helloworld')
            label1 = Label(self, text="Unit 2 State:", bg="lightblue").grid(row=0, column=3, sticky='nsew')
            label2 = Label(self, textvariable=unit2Label, bg="lightblue", font=30).grid(row=1, column=3, sticky='nsew')


            canvasB = FigureCanvasTkAgg(b, self)
            canvasB.show()
            canvasB.get_tk_widget().grid(row=2, column=0, columnspan=4)
            self.canvas = canvasB

    # Unit 3 data page
    class GraphPageC(tk.Frame):

        def __init__(self, parent, controller):
            global unit3Label
            tk.Frame.__init__(self, parent)
            button1 = tk.Button(self, text="Go to Unit 1", width=WIDTH, command=(lambda: controller.show_frame(GraphPageA)))
            button1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
            button2 = tk.Button(self, text="Go to Unit 2", width=WIDTH, command=(lambda: controller.show_frame(GraphPageB)))
            button2.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
            button3 = tk.Button(self, text="Go to Unit 3", width=WIDTH, bd=2, bg='green')
            button3.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
            button4 = tk.Button(self, text="State Control", width=WIDTH, command=(lambda: controller.show_frame(StateHandler)))
            button4.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
            slider = tk.Scale(self, from_=10, to=200, orient=HORIZONTAL, bg="lightblue")
            slider.grid(row=0, column=2, sticky='nsew')
            button5 = tk.Button(self, text="Scale", width=WIDTH, bg="lightblue", command=(lambda: ranging_function(slider.get())))
            button5.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

            unit3Label = StringVar()
            unit3Label.set('helloworld')
            label1 = Label(self, text="Unit 3 State:", bg="lightblue").grid(row=0, column=3, sticky='nsew')
            label2 = Label(self, textvariable=unit3Label, bg="lightblue", font=30).grid(row=1, column=3, sticky='nsew')

            canvasC = FigureCanvasTkAgg(c, self)
            canvasC.show()
            canvasC.get_tk_widget().grid(row=2, column=0, columnspan=4)
            self.canvas = canvasC

    # state control
    class StateHandler(tk.Frame):

        def __init__(self, parent, controller):
            # self.parent = parent
            # self.poll()

            tk.Frame.__init__(self, parent)
            # change page buttons
            button = tk.Button(self, text="Go to Unit 1", width=WIDTH+OFFSET
                                , command=lambda: controller.show_frame(GraphPageA))
            button.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

            button2 = tk.Button(self, text="Go to Unit 2", width=WIDTH+OFFSET
                                , command=lambda: controller.show_frame(GraphPageB))
            button2.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

            button3 = tk.Button(self, text="Go to Unit 3", width=WIDTH+OFFSET
                                , command=lambda: controller.show_frame(GraphPageC))
            button3.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

            button4 = tk.Button(self, text="State Control", bd=2, bg='green', width=WIDTH+OFFSET)

            button4.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
            # state selection buttons
            # Unit 1 state
            button5 = tk.Button(self, text="Import",
                                command=lambda: state_control_function(B1_marker=True, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button5.grid(row=4, column=2, sticky='nsew', ipadx=1, pady=5)

            button6 = tk.Button(self, text="Export",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=True, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button6.grid(row=4, column=3, sticky='nsew', ipadx=1, pady=5)

            button7 = tk.Button(self, text="Reset",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=True,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button7.grid(row=4, column=4, sticky='nsew', ipadx=4, pady=5)
            # Unit 2 state
            button8 = tk.Button(self, text="Import",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=True, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button8.grid(row=5, column=2, sticky='nsew',ipadx=1, pady=5)

            button9 = tk.Button(self, text="Export",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=True, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button9.grid(row=5, column=3, sticky='nsew', ipadx=1, pady=5)

            button10 = tk.Button(self, text="Reset",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=True,
                                        B7_marker=False, B8_marker=False, B9_marker=False))
            button10.grid(row=5, column=4, sticky='nsew', ipadx=1, pady=5)

            # Unit 3 state
            button11 = tk.Button(self, text="Import",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=True, B8_marker=False, B9_marker=False))
            button11.grid(row=6, column=2, sticky='nsew', ipadx=1, pady=5)

            button12 = tk.Button(self, text="Export",
                                 command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=True, B9_marker=False))
            button12.grid(row=6, column=3, sticky='nsew', ipadx=1, pady=5)

            button13 = tk.Button(self, text="Reset",
                                command=lambda: state_control_function(B1_marker=False, B2_marker=False, B3_marker=False,
                                        B4_marker=False, B5_marker=False, B6_marker=False,
                                        B7_marker=False, B8_marker=False, B9_marker=True))
            button13.grid(row=6, column=4, sticky='nsew', ipadx=1, pady=5)

            # state execution button
            button11 = tk.Button(self, text="Confirm State Change", command=lambda: state_exe())
            button11.grid(row=3, column=0, sticky='nsew', padx=80, pady=80, columnspan=2, rowspan=4)


    # run programs and enter GUI loop
    stateOut = statemodule.State('reset', 'reset', 'reset')
    stateIn = statemodule.State('reset', 'reset', 'reset')
    worker_init()
    app = HUGGUI()
    app.geometry("1000x600")
    aniA = animation.FuncAnimation(a, updateGraphsA, interval=500, blit=False)
    aniB = animation.FuncAnimation(b, updateGraphsB, interval=500, blit=False)
    aniC = animation.FuncAnimation(c, updateGraphsC, interval=500, blit=False)
    app.after(1, state_update)
    app.mainloop()
    poison_pill()
