<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
/* eslint-disable */

import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5002/ping';

      const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzYW1wbGUtYXV0aC1zZXJ2ZXIiLCJleHAiOjE1NjAwODczMzUuMTc1MDgxNX0.POdimsTalYEdWRGpNQYJ_ZFAnetxClwSmN-r6v5uByIGSyrMN3giCcIn0czO6gveTbfbmnHQSYa1HjpUMAoBZmeyGcwVcbQyiFvd_aalP_SIAR71Sq7FJ_qkrwkYVGT4UZPlsciK8pnXs4hSbqiXVqXu5qt16q8tsAbBBJBgCNyhRJ1fzrFizgRKo4vS0RMyyNBGIZ-bUxvUCO8Go1jxrcWAAm3MO3r_br73c2m5NpsKhHlMeJbTfc5a9MP3ChLX0BQM-pipLlpRIIn_Yw_fMyMCvuwL3rcpm5XCaRS5tUBVbBzu4mTS5ru7V6-SYhu8KBvcTdug_Y9af8Xe6jDrlg';

      const config = {
          headers: {'authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'},
      };
 
      axios.get(path, config)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
