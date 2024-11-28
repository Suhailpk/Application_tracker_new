import React, { useEffect, useState } from 'react'
import AxiosInstance from "../api";
import { List, ListItem, ListItemText, Button, Box, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const ApplicationList = () => {
  const navigate = useNavigate();
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)

  const getData = async()=>{
    try{
      const appResponse = await AxiosInstance.get(`api/applications`)
      console.log("app reponse ------>", appResponse.data)
      setData(appResponse.data)
      setLoading(false)
    }catch(error){
      console.log('error in fetching data ------->', error)
    }
  }

  useEffect(()=>{
    getData()
  },[])

  // Example list items
  const items = [
    { id: 1, name: 'Item 1', description: 'Description for item 1' },
    { id: 2, name: 'Item 2', description: 'Description for item 2' },
    { id: 3, name: 'Item 3', description: 'Description for item 3' },
    { id: 4, name: 'Item 4', description: 'Description for item 4' },
  ];

  // Handle "Show All" button click
  const handleShowAll = () => {
    navigate('/application_detail'); // Replace with your desired route
  };

  return (
    <div>
    {loading? <p>Loading data ..........</p>:
    <Box sx={{ display: 'flex', alignItems: 'flex-start', mt: 4 }}>
      <Box 
        sx={{ 
          width: '25%', 
          p: 3, 
          boxShadow: 3, 
          borderRadius: 2, 
          backgroundColor: '#fff',
          mr: 2 // Add some spacing to the right
        }}
      >
        <Typography variant="h5" gutterBottom>
          List of Items
        </Typography>

        <List>
          {data.map((item) => (
            <ListItem key={item.id} divider>
              <ListItemText primary={item.company_name} secondary={item.position} />
            </ListItem>
          ))}
        </List>

        <Button
          variant="contained"
          color="primary"
          fullWidth
          sx={{ mt: 3 }}
          onClick={handleShowAll}
        >
          Show All
        </Button>
      </Box>
    </Box>
    }
    </div>
  );
};

export default ApplicationList;
