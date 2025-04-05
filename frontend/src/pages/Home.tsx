import React from 'react';
import { Grid, Card, CardContent, CardActions, Typography, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const subjects = [
  { id: 'coding', name: 'Coding', description: 'Learn programming and coding' },
  { id: 'visual_arts', name: 'Visual Arts', description: 'Explore drawing, painting, and design' },
  { id: 'performing_arts', name: 'Performing Arts', description: 'Learn music, dance, and theater' },
  { id: 'financial_literacy', name: 'Financial Literacy', description: 'Understand money management' },
  { id: 'science', name: 'Science', description: 'Discover scientific concepts and experiments' },
];

const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Welcome to TAPBuddy!
      </Typography>
      <Typography variant="subtitle1" gutterBottom align="center" sx={{ mb: 4 }}>
        Your AI-powered learning assistant. Choose a subject to start learning!
      </Typography>
      
      <Grid container spacing={3}>
        {subjects.map((subject) => (
          <Grid item xs={12} sm={6} md={4} key={subject.id}>
            <Card>
              <CardContent>
                <Typography variant="h5" component="h2" gutterBottom>
                  {subject.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {subject.description}
                </Typography>
              </CardContent>
              <CardActions>
                <Button
                  size="small"
                  color="primary"
                  onClick={() => navigate(`/subject/${subject.id}`)}
                >
                  Start Learning
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default Home; 