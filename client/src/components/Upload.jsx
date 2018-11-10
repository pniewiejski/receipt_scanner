import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import { withStyles }  from '@material-ui/core/styles';

const styles = theme => ({
    button: {
      margin: theme.spacing.unit,
    },
    rightIcon: {
      marginLeft: theme.spacing.unit,
    },
    input: {
        display: "none"
    }
  });

class Upload extends Component {
    
    

    render() {
        const { classes } = this.props;
            return (
                <div>
                <input
                        accept="image/*"
                        className={classes.input}
                        id='contained-button-file'
                        type="file"
                    />
                <label htmlFor='contained-button-file'>
                <Button 
                variant="contained" 
                component='span'
                className={classes.button}
                size='large'
                color="primary"
                disableRipple={true}
                >
                Upload
                <CloudUploadIcon className={classes.rightIcon} />
              </Button>
              </label>
              </div>
              );
    }
}

export default withStyles(styles)(Upload);