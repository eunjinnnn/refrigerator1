<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-green-700 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<Navbar let:NavContainer color="green">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">REFRIGERATOR</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass}>
    <NavLi href="/">Home</NavLi>
    <NavLi href="/edit">EDIT</NavLi>
    <NavLi href="/my_refrigerator">MY REFRIGERATOR</NavLi>
    <NavLi href="/food_diary">FOOD DIARY</NavLi>
    <NavLi href="/receipe">RECEIPE</NavLi>
  </NavUl>
</Navbar>

<div class="px-2 sm:px-4">
    <div class="container mx-auto">
        <slot></slot>
    </div>
</div>
