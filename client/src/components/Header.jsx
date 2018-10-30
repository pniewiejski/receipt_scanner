import React, { Component } from 'react';
import {withStyles} from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid'
import Typography from '@material-ui/core/Typography';
import logo from '../images/receipt.svg';

const styles = theme => ({
logoIcon: {
    fontSize: '48px'
},

});

class Header extends Component {
    render(){
        return(
            <Grid
            container
            className='headerWrapper'
            spacing={24}
            direction='row'
            alignItems='center'
            justify="center"
            >
                <Grid item>
                <img
            src={logo}
            alt=''
            width='200px'
            />
                </Grid>
                <Grid item>
                <Typography component="h2" variant="h1" gutterBottom>
            Receipt Scanner
                 </Typography>
                </Grid>
            </Grid>
        );
    }
}
export default withStyles(styles)(Header);