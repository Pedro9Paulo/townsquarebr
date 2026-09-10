<template>
  <div class="intro">
    <img src="static/apple-icon.png" alt="" class="logo" />
    <div>
      Bem-vinde ao
      <b>Grimório e Praça virtual</b> não-oficial de Blood on the Clocktower!
      Por favor adicionar mais jogadores pelo
      <span class="button" @click="toggleMenu">
        <font-awesome-icon icon="cog" /> Menu
      </span>
      no canto superior direito ou apertando <b>[A]</b>. Você também pode se juntar a uma
      partida apertando <b>[J]</b>.<br />
      <div class="footer">
        Essa projeto e tradução são grátis e código aberto e poder ser encontrado em:
        <a href="https://github.com/Pedro9Paulo/townsquarebr" target="_blank"
          >GitHub</a
        >. Isso não é afiliado ao The Pandemonium Institute ou Across the Board. "Blood on the
        Clocktower" é uma marca registrada de Steven Medway and The Pandemonium Institute.
        Oficialmente localizada para o Brasil pela Across the Board        
      </div>
    </div>
    <img src="../assets/community-created-content.webp" alt="" class="ccc" />
    <a
      class="redirect"
      v-if="language === 'zh-CN'"
      href="https://clocktower.gstonegames.com"
    >
      <img src="../assets/gstone.webp" class="gstone" alt="" />
      你想使用中文版魔典吗？
    </a>
  </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      language: window.navigator.userLanguage || window.navigator.language,
    };
  },
  methods: mapMutations(["toggleMenu"]),
};
</script>

<style scoped lang="scss">
.intro {
  text-align: center;
  width: 50%;
  font-size: 120%;
  position: absolute;
  padding: 10px;
  background: rgba(0, 0, 0, 0.5);
  border: 3px solid black;
  border-radius: 10px;
  z-index: 3;
  display: flex;
  justify-content: center;
  a {
    color: white;
  }
  a.redirect {
    display: block;
    text-decoration: none;
    position: absolute;
    top: 100%;
    margin-top: 2vh;
    padding: 10px;
    background: rgba(0, 0, 0, 0.5);
    border: 3px solid black;
    border-radius: 10px;

    &:hover {
      color: red;
    }
    img {
      width: 120px;
      display: block;
      margin: auto auto 1vh;
    }
  }

  img.logo {
    position: absolute;
    bottom: 100%;
    width: 25vh;
    margin-bottom: 2vh;
    max-width: 192px;
    border-radius: 50%;
    box-shadow: 0 0 10px black;
    border: 3px solid black;
  }

  img.ccc {
    position: absolute;
    top: 100%;
    width: 25vh;
    margin-top: 2vh;
    max-width: 192px;
    filter: drop-shadow(0 0 10px black);
  }

  .footer {
    font-size: 60%;
    opacity: 0.75;
  }
}
</style>
