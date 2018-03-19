import React, { Component } from 'react';
import Chart from 'chart.js';

class Plot extends Component {
    constructor(props) {
        super(props);
        this.state = {  }
    }

    componentDidUpdate(prevProps, prevState) {
        if (this.props.data) {
            this.renderData();
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
