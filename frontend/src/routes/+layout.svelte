<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { onMount } from 'svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-zinc-200 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:bg-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';

  let isMenuOpen = false;
  function closeMenu() {
    isMenuOpen = false;
  }
  function openMenu() {
    isMenuOpen = !isMenuOpen;
    console.log(isMenuOpen);
  }

  $: $page.url.pathname, closeMenu();

  onMount(() => {
    closeMenu();
  });

</script>

<Navbar class="fixed top-0 left-0 w-full z-50 bg-orange-50/60 flex items-center justify-between px-4 py-2 shadow-md border-b border-gray-300">
  <NavBrand href="/">
    <h1 class="text-3xl sm:text-xl font-grandstander font-semibold text-amber-950 mt-2">FRESHKEEP</h1>
  </NavBrand>
  <NavHamburger onClick={openMenu} />
    <NavUl {activeUrl} {activeClass} {nonActiveClass} class="items-center w-full bg-zinc-50/70" hidden={isMenuOpen? false : true}>
      <NavLi href="/my_refrigerator" class="font-grandstander text-amber-950 hover:bg-zinc-200 transition-colors duration-300" on:click={closeMenu}>MY REFRIGERATOR</NavLi>
      <NavLi href="/food_diary" class="font-grandstander text-amber-950 hover:bg-zinc-200 transition-colors duration-300" on:click={closeMenu}>FOOD DIARY</NavLi>
      <NavLi href="/receipe" class="font-grandstander text-amber-950 hover:bg-zinc-200 transition-colors duration-300" on:click={closeMenu}>RECEIPE</NavLi>
    </NavUl>
</Navbar>


<!-- stone-200 -->
<div class="min-h-screen bg-cover bg-center" style="background-image: url('/images/bg1.jpg');">
  <div class="min-h-80 p-2 sm:p-4">
      <div class="flex flex-col">
        <div class="mt-16 px-3">
          <slot></slot>
        </div>
      </div>
  </div>
</div>

<style>
  .bg-cover {
    background-size: cover;
  }
  .bg-center {
    background-position: center;
  }
</style>
