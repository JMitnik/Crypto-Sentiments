import React, { Component } from 'react';
import CSVReader from 'react-csv-reader';
import Plot from './Plot';
import moment from 'moment';

class BitcoinValues extends Component {
    constructor(props) {
        super(props);
        this.state = {
            bitcoinList: []
        }
    }

    fetchBitcoinValues = (event) => {
        if (this.props.activeStartDate) {
            let sd = moment(this.props.activeStartDate).format('YMMDD')
            let ed = moment(this.props.activeEndDate).format('YMMDD')
            fetch(`http://127.0.0.1:5000/date/months?start_date=${sd}&end_date=${ed}`)
            .then(res => res.json())
            .then(data => this.setState({bitcoinList: data.result}));
        }
    }

    getBitcoinValues = () => {
        if (this.state.bitcoinList) {
            return {
                'x_axis': this.state.bitcoinList.map(el => el['Date']).reverse(),
                'y_axis': this.state.bitcoinList.map(el => el['Open']).reverse()
            };
        }
    }

    render() {
        return (
            <div>
                <div onClick={e => this.fetchBitcoinValues(e)} className="btn btn-secondary">Get Crypto Values!</div>
                {/* <CSVReader onFileLoaded={this.handleCryptoCSV}></CSVReader> */}
                <Plot data={this.getBitcoinValues()}></Plot>
            </div>
         );
    }
}

export default BitcoinValues;
