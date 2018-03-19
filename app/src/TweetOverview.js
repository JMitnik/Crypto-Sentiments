import React, { Component } from 'react';
import List from './List';
import Chart from 'chart.js';

const TWEET_URL = `http://127.0.0.1:5000/tweets`;

class TweetOverview extends Component {
    state = {
        tweetDays: [],
        activeDay: null
    }

    fetchTweets = (event) => {
        event.preventDefault();
        console.log(event);

        fetch(TWEET_URL)
        .then(res => res.json())
        .then(data => this.setState({tweetDays: data}));
    }

    componentDidMount() {
        this.insertChart();
    }

    insertChart = () => {

    }

    render() {
        return (
            <div>
                <div>
                    <button onClick={e => this.fetchTweets(e)}></button>
                </div>
                <canvas id="test-chart" className="test-chart"></canvas>
            </div>
        )
    }
 }

export default TweetOverview;
