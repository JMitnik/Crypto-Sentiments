import React, { Component } from 'react';
import CSVReader from 'react-csv-reader';
import Plot from './Plot';

class BitcoinValues extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bitcoinList: [],
            selectedDate: new Date(2017, 10, 11).toDateString()
        }
    }

    handleCryptoCSV = (data) => {
        this.setState({bitcoinList: data});
    }

    getBitcoinValues = () => {
        if (this.state.bitcoinList) {
            return {
                'x_axis': this.state.bitcoinList.slice(1).map(el => el[1]),
                'y_axis': this.state.bitcoinList.slice(1).map(el => parseInt(el[3]))
            };
        }
    }

    goBackInTime = () => {
        let dateObj = new Date(this.state.selectedDate);

        dateObj.setDate(dateObj.getDate() - 1);
        this.setState({ selectedDate: dateObj.toDateString()})
    }

    goForwardInTime = () => {
        let dateObj = new Date(this.state.selectedDate);

        dateObj.setDate(dateObj.getDate() + 1);
        this.setState({ selectedDate: dateObj.toDateString() })
    }

    render() {
        return (
            <div>
                <div>
                    <span onClick={this.goBackInTime} className="btn btn-primary"> Back </span>
                    <span>Selected Date: {this.state.selectedDate}</span>
                    <span onClick={this.goForwardInTime} className="btn btn-primary"> Forward </span>
                </div>
                <CSVReader onFileLoaded={this.handleCryptoCSV}></CSVReader>
                <Plot data={this.getBitcoinValues()}></Plot>
            </div>
         );
    }
}

export default BitcoinValues;
