import React, { Component } from 'react';
import values from './bitcoin-values.csv';
import BitcoinValues from './BitcoinValues';
import TweetList from './TweetList';
// import WordCloud from './WordCloud';
import DatePicker from './DataPicker';

class DataBoard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeStartDate: null,
            activeEndDate: null
         }
    }

    getDateRange = (startDate, endDate) => {
        if (startDate || endDate) {
            this.setState({activeStartDate: startDate, activeEndDate: endDate});
        }
    }

    render() {
        return (
            <div>
                <DatePicker getDateRange={(activeStartDate, activeEndDate) => this.getDateRange(activeStartDate, activeEndDate)}></DatePicker>
                <BitcoinValues activeStartDate={this.state.activeStartDate} activeEndDate={this.state.activeEndDate}></BitcoinValues>
                {/* <TweetList activeDate={this.state.activeDate}></TweetList> */}
                {/* <WordCloud activeDate={this.state.activeDate}></WordCloud> */}
            </div>
         );
    }
}

export default DataBoard;
