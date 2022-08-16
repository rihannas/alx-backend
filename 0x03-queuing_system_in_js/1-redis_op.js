import * as redis from 'redis';
const redisClient = redis.createClient();

redisClient.connect()

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, (error, reply) => {
      redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (error, reply) => {
      console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
