import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((resolve) => {
      const photo = resolve[0];
      const user = resolve[1];
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
