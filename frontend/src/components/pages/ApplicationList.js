import * as React from 'react';
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import { FixedSizeList } from 'react-window';
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';

function renderRow(props) {
  const { index, style } = props;

  return (
    <ListItem style={style} key={index} component="div" disablePadding>
      <ListItemButton>
        <ListItemText primary={`Item ${index + 1}`} />
      </ListItemButton>
    </ListItem>
  );
}

export default function ApplicationList() {
  return (
    <><Box
          sx={{ width: '50%', height: 300, bgcolor: 'grey' }}
      >
          <FixedSizeList
              height={400}
              width={360}
              itemSize={46}
              itemCount={6}
              overscanCount={5}
          >
              {renderRow}
          </FixedSizeList>
      </Box><Button component={Link} to={'/application_detail'}>
              Show All
          </Button></>
  );
}
