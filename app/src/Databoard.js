import React, { Component } from 'react';
import values from './bitcoin-values.csv';
import BitcoinValues from './BitcoinValues';

class DataBoard extends Component {
    constructor(props) {
        super(props);
        this.state = {  }
    }

    render() {
        return (
            <div>
                <BitcoinValues></BitcoinValues>
            </div>
         );
    }
}

export default DataBoard;
