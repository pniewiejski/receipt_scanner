import React, {
    Component
} from 'react';
import Grid from '@material-ui/core/Grid';
import Upload from './Upload';
import Logo from './Header';
import {withStyles} from '@material-ui/core/styles'
import PropTypes from "prop-types";

const styles = theme => ({
    root: {
        backgroundColor: theme.palette.primary.light,
        minHeight: "100vh"
    }
});

class Home extends Component {
    render() {
        const { classes } = this.props;
        return (
            <Grid
            container
            spacing={0}
            className={classes.root}
            direction = "column"
            alignItems = "center"
            justify = 'center'
            >

                <Grid item xs={12}>
                    <Logo />
                </Grid>
                <Grid item xs={12}>
                    <Upload />
                </Grid>

            
            </Grid>
       
        );
    }
}

Home.propTypes = {
    classes: PropTypes.object.isRequired
  };
export default withStyles(styles)(Home);