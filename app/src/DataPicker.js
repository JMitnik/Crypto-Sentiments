import React, { Component } from 'react';

const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

class DataPicker extends Component {
    constructor(props) {
        super(props);

        this.state = {
            activeStartDate: null,
            activeEndDate: null
        };
    }

    componentDidMount() {
        let initStartDate = new Date().toDateString();
        let initEndDate = this.getNextMonth(initStartDate);
        this.setState({activeStartDate: initStartDate, activeEndDate: initEndDate});
    }

    getPrevMonth = (date) => {
        let dateObj = new Date(date);
        dateObj.setMonth(dateObj.getMonth() - 1);
        return dateObj;
    }

    getNextMonth = (date) => {
        let dateObj = new Date(date);
        dateObj.setMonth(dateObj.getMonth() + 1);
        return dateObj.toDateString();
    }

    goBackInTime = () => {
        // For now, let's do this for a month
        let newEndDate = this.state.activeStartDate;
        let prevMonth = this.getPrevMonth(this.state.activeStartDate);
        this.setState({ activeStartDate: prevMonth, activeEndDate: newEndDate });
        this.props.getDateRange(prevMonth, newEndDate);
    }

    goForwardInTime = () => {
        // For now, let's do this for a month
        let newEndDate = this.state.activeStartDate;
        let prevMonth = this.getNextMonth(this.state.activeStartDate);
        this.setState({ activeStartDate: prevMonth, activeEndDate: newEndDate });
        this.props.getDateRange(prevMonth, newEndDate);
    }

    getPublicDate = () => {
        let dateObj = new Date(this.state.activeStartDate);
        return monthNames[dateObj.getMonth()];
    }

    render() {
        return (
            <div>
                <button onClick={this.goBackInTime} className="btn btn-primary btn-sm m">
                    Prev
                </button>
                <span className="text-info">{this.getPublicDate()}</span>
                <button onClick={this.goForwardInTime} className="btn btn-primary btn-sm m">
                    Next
                </button>
            </div>
        )
    }
}

export default DataPicker;
