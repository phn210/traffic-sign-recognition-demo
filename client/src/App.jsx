import React from "react";
import { AppBar, Toolbar } from "@material-ui/core";
import { Container, Grid, CssBaseline } from "@material-ui/core";
import { Card, CardContent, CardMedia, CardActions } from "@material-ui/core";
import { Button } from "@material-ui/core";
import { Input, InputLabel, Select, MenuItem } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { PhotoCamera } from '@material-ui/icons';
import useStyles from "./styles";

const App = () => {
    const classes = useStyles();
    const [prediction, setPrediction] = React.useState('');

    const handleChange = (event) => {
        setPrediction(event.target.value);
    };

    return (
        <>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                    {/* <CameraIcon className={classes.icon} /> */}
                    <Typography variant="h6" color="inherit" noWrap>
                        Traffic Signs Recoginiton
                    </Typography>
                </Toolbar>
            </AppBar>
            <main>
                <div>
                    <Container maxWidth="sm">
                        <Typography variant="h2" align="center" color="textPrimary" gutterBottom>
                            Upload File
                        </Typography>
                        <Typography variant="h5" align="center" color="textSecondary" gutterBottom>
                            Your file will be process after successfully uploaded
                        </Typography>
                    </Container>
                </div>
                <Container className={classes.cardGrid} maxWidth="md">
                    <Grid container spacing={4}>
                        <Grid item xs={4}>
                            <Card className={classes.card}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image="./logo512.png"
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography>
                                        Upload your content here
                                    </Typography>
                                </CardContent>
                                <CardActions className={classes.cardActions}>
                                    <Button size="small" variant="contained" color="primary">Upload</Button>
                                    <InputLabel id="img-method-select-1-label">Method</InputLabel>
                                    <Select
                                        labelId="img-method-select-1-label"
                                        id="img-method-select-1"
                                        value={prediction}
                                        onChange={handleChange}
                                        label="Prediction Method"
                                    >
                                        <MenuItem value="">
                                            <em>None</em>
                                        </MenuItem>
                                        <MenuItem value={'CNN'}>CNN</MenuItem>
                                        <MenuItem value={'VGG16'}>VGG16</MenuItem>
                                        <MenuItem value={'YOLO'}>YOLO</MenuItem>
                                    </Select>
                                </CardActions>
                            </Card>
                        </Grid>
                        <Grid item xs={4}>
                            <Card className={classes.card}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image="./logo512.png"
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography>
                                        Test
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small" color="primary">Upload</Button>
                                    <Input></Input>
                                </CardActions>
                            </Card>
                        </Grid>
                        <Grid item xs={4}>
                            <Card className={classes.card}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image="./logo512.png"
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography>
                                        Test
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small" color="primary">Upload</Button>
                                    <Input></Input>
                                </CardActions>
                            </Card>
                        </Grid>
                    </Grid>
                    
                </Container>
            </main>
        </>
    );
}

export default App;