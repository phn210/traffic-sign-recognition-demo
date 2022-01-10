import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    container: {

    },

    cardGrid: {
        padding: "20px 0",
        display: "flex",
        flexDirection: "row"
    },

    card: {
        height: '100%',
        
    },

    cardMedia: {
        paddingTop: '100%'
    },

    cardContent: {
        // flexGrow: 1,
    },

    cardActions: {
        padding: "0 0 0 1rem"
    }

}));

export default useStyles;