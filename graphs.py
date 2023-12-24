import pyqtgraph as pg


class Graphs:
    @staticmethod
    def traffic_consumption():
        # Plot Traffic Consumption graph
        traffic_consumption_graph = pg.PlotWidget()
        traffic_consumption_graph.setBackground((9, 5, 13))

        # Plot the main line
        traffic_consumption_graph.plot([2.9, 3.5, 3.4, 3.5, 4, 3.7, 3.8, 4.2],
                                       pen=pg.mkPen(color='#3C3246', width=2.5),
                                       symbol='o',
                                       symbolBrush='#3C3246',
                                       symbolPen=pg.mkPen(color='#3C3246'))

        # Hiding axis
        traffic_consumption_graph.getPlotItem().hideAxis('left')
        traffic_consumption_graph.getPlotItem().hideAxis('bottom')

        return traffic_consumption_graph

    @staticmethod
    def energy_consumption():
        # Plot Energy Consumption graph
        electricity_consumption_graph = pg.PlotWidget()
        electricity_consumption_graph.setBackground((9, 5, 13))

        # Plot the main line
        electricity_consumption_graph.plot([1, 3, 2, 4], pen=pg.mkPen(color='#E60540', width=2.5))

        # Add custom ticks
        custom_ticks = [(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thu'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')]
        electricity_consumption_graph.getAxis('bottom').setTicks([custom_ticks])

        return electricity_consumption_graph

    @staticmethod
    def devices():
        # Plot devices graph
        devices_graph = pg.PlotWidget()
        devices_graph.setBackground((9, 5, 13))

        # Plot the main lines
        curve_mobile = devices_graph.plot([4.2, 5, 4.2, 4.6], pen=pg.mkPen(color='#05A7D1', width=2.5))
        curve_computer = devices_graph.plot([4.6, 4.4, 4.7, 4.8], pen=pg.mkPen(color='#B4CC5D', width=2.5))
        curve3_laptop = devices_graph.plot([4, 4.8, 4.3, 4.4], pen=pg.mkPen(color='#E60540', width=2.5))

        # Add legend
        legend = devices_graph.addLegend()
        legend.addItem(curve_mobile, name="Mobile")
        legend.addItem(curve_computer, name="Computer")
        legend.addItem(curve3_laptop, name="Laptop")

        return devices_graph
