import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
    .then((resolve) => resolve.map((promise) => ({
      status: promise.status,
      value: promise.status === 'fulfilled' ? promise.value : `${promise.reason.name}: ${promise.reason.message}`,
    })));
}
