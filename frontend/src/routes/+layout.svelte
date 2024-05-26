<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-lime-950 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-lime-950 hover:bg-stone-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';

  let categories = [
      { id: 1, name: 'VEGETABLES' },
      { id: 2, name: 'DRINKS' },
      { id: 3, name: 'FROZEN FOOD' },
      { id: 4, name: 'ETC' }
  ];

  let item_list = [
      { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24' },
      { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23' },
      { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05' },
      { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07' },
      { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28' },
      { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06' },
      { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06' },
      { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06' },
  ];

  let units = [
      { value: 1, name: '개' },
      { value: 2, name: 'L' },
      { value: 3, name: '조각' }
  ];

  let lists = [];
  let cat_selected = '';
  let unit_selected = '';
  let volume = '';
  let foodname = '';
  let purchaseDate = '';
  let expirationDate = '';

  let isFormVisible = false;


  function filteredItems(categoryId) {
      return item_list.filter(item => item.category === categoryId).sort((a, b) => {
          return new Date(a.expiration_date) - new Date(b.expiration_date);
  });
  }

  function isExpired(expiration_date) {
      return new Date(expiration_date) < new Date();
  }

  function toggleFormVisibility() {
      isFormVisible = !isFormVisible;
  }

  function addItem(event) {
      event.preventDefault();
      const selectedCategory = categories.find(cat => cat.value == cat_selected)?.name || '';
      const selectedUnit = units.find(unit => unit.value == unit_selected)?.name || '';

      lists.push({
          foodname,
          volume,
          unit: selectedUnit,
          category: selectedCategory,
          purchaseDate,
          expirationDate
      });

      foodname = '';
      volume = '';
      unit_selected = '';
      cat_selected = '';
      purchaseDate = '';
      expirationDate = '';
  }

</script>

<Navbar class="bg-lime-950">
  <NavBrand href="/">
    <span class="self-center font-serif text-orange-50 whitespace-nowrap text-lg font-semibold">My Refrigerator</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass} color = 'bg-orange-50'>
    <NavLi href="/my_refrigerator" size="sm" class="font-serif text-sm border-b-2 border-transparent hover:border-lime-950">MY REFRIGERATOR</NavLi>
    <NavLi href="/food_diary" size="sm" class="font-serif text-sm border-b-2 border-transparent hover:border-lime-950">FOOD DIARY</NavLi>
    <NavLi href="/receipe" size="sm" class="font-serif text-sm border-b-2 border-transparent hover:border-lime-950">RECEIPE</NavLi>
  </NavUl>
</Navbar>

<div class="min-h-screen bg-orange-50">
  <div class="py-2 sm:py-4 px-2 sm:px-4">
      <div class="container mx-auto">
          <slot></slot>
      </div>
  </div>
</div>

