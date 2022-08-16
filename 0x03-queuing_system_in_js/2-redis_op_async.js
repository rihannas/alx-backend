import * as redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();
const asyncGet = promisify(redisClient.get).bind(redisClient);

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

async function displaySchoolValue(schoolName) {
  const value = await asyncGet(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
