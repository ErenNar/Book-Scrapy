<template>
  <header class="py-5">
    <HeaderSection :url="url"  v-model:link="link"  :sendForm="sendForm" ></HeaderSection>
   
  </header>
  <main class="py-5">
    <MainBookSection :loading="loading" :filterDataBook="filterDataBook" :dataBook="dataBook" :deleteProduct="deleteProduct"  ></MainBookSection>
  </main>
</template>
<script>
import axios from "axios";
import { keys } from "../key.js";
import HeaderSection from "./components/HeaderSection.vue";
import MainBookSection from "./components/MainBookSection.vue";
import './assets/main.css'
export default {
  name:'Book App',
  components: {
    HeaderSection,
    MainBookSection
  },
  data() {
    return {
      url: keys.URL,
      loading: true,
      dataBook: [],
      filterDataBook: [],
      link:''
    };
  },
  methods: {
    sendForm() {
      const link = this.link;
      console.log(this.link);
      
      if (link === "") {
        alert("Required");
      } else {
        this.loading = true;
        try {
          axios({
            method: "post",
            url: keys.INSERT_URL,
            data: {
              link: this.link,
            },
          })
            .then((data) => {
              console.log(data);
            })
            .catch((err) => {
              console.log(err);
            })
            .finally(() => {
              setTimeout(() => {
                this.loading = false;
                location.reload();
              }, 2000);
            });
        } catch (error) {
          console.log(error);
        }
      }
    },
    deleteProduct(id) {
      this.loading = true;
      axios({
        method: "post",
        url: keys.DELETE_URL,
        data: {
          id: id,
        },
      })
        .then((data) => {
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
        })
        .finally(() => {
          setTimeout(() => {
            this.loading = false;
            location.reload();
          }, 2000);
        });
    },
  },
  computed: {
    async bookFind() {
      try {
        const req = await axios.get(keys.FIND_URL);
        const res = req.data;

        if (req.status == 200) {
          setTimeout(() => {
            this.dataBook = res;

            this.loading = false;
          }, 2000);
        }
      } catch (error) {
        console.log(error);
      }
    },
    async bookLimitFind() {
      try {
        const req = await axios.get(keys.LIMIT_URL);
        const res = req.data;

        if (req.status == 200) {
          setTimeout(() => {
            this.filterDataBook = res;
            this.loading = false;
          }, 2000);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },

  mounted() {
    this.bookFind;
    this.bookLimitFind;
  },
};
</script>
