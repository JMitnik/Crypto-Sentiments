import React, { Component } from 'react';
import Chart from 'chart.js';

class Plot extends Component {
    constructor(props) {
        super(props);
        this.state = {
            intialized: false
        }

        this.chart = null;
    }

    componentDidUpdate(prevProps, prevState) {
        if (!this.state.intialized) {
            if (this.props.data) {
                this.renderData();
            }
        } else {
            this.chart.update();
        }
    }

    renderData = () => {
        const canvas = document.getElementById('plot');
        var myChart = new Chart(canvas, {
            type: 'line',
            data: {
                labels: this.props.data.x_axis,
                datasets: [{
                    label: 'Bitcoin to $USD',
                    data: this.props.data.y_axis
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });

        // this.setState({intialized: true});
        // this.chart = myChart;
        // console.log(this.chart);
    }

    render() {
        return (
            <div>
                <canvas id="plot"></canvas>
            </div>
        );
    }
}

export default Plot;
