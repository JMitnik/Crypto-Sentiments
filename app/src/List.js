import React, { Component } from 'react';
import ListItem from './ListItem';

const List = (props) =>
    // Object.keys(props.items).forEach(item => <ListItem item={item}></ListItem>);

    <div>
        {props.items.map(item => <RowEl item={item}></RowEl>)}
    </div>

export default List;

const RowEl = (props) =>
    <div>
        Date is: {props.item.date}
    </div>
