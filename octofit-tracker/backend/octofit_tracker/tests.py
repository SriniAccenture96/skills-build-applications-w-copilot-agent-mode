from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team2', description='desc')
        user = User.objects.create(email='test@example.com', name='Test User', team=team, is_superhero=True)
        self.assertEqual(str(user), 'test@example.com')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team3', description='desc')
        user = User.objects.create(email='test2@example.com', name='Test User2', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Run', duration_minutes=10, date='2025-01-01')
        self.assertEqual(str(activity), 'test2@example.com - Run')

    def test_workout_create(self):
        team = Team.objects.create(name='Test Team4', description='desc')
        workout = Workout.objects.create(name='Workout', description='desc', suggested_for_team=team)
        self.assertEqual(str(workout), 'Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team5', description='desc')
        leaderboard = Leaderboard.objects.create(team=team, total_points=50)
        self.assertEqual(str(leaderboard), 'Test Team5 - 50 points')
